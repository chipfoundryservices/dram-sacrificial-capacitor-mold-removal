"""Check book completeness, local links, independent numerical targets and build integrity."""
from pathlib import Path
import argparse
import hashlib
import json
import math
import re
from html.parser import HTMLParser
from calculations import calculate

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.hrefs.append(attrs['href'])


def validate(dist=False):
    chapters = sorted((ROOT / 'chapters').glob('*.md'))
    appendices = sorted((ROOT / 'appendices').glob('*.md'))
    assert len(chapters) == 16, 'Expected 16 chapters'
    assert [p.name[:2] for p in chapters] == [f'{i:02}' for i in range(1, 17)]
    assert [p.name[0] for p in appendices] == list('ABCDEFG')
    for path in chapters:
        text = path.read_text()
        assert '## Study questions' in text, f'Missing questions: {path}'
        assert len(text.split()) >= 250, f'Chapter too short: {path}'
    docs = [*ROOT.glob('*.md'), *chapters, *appendices, * (ROOT / 'research').glob('*.md')]
    links = 0
    for path in docs:
        text = path.read_text()
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith(('http://', 'https://', '#')):
                continue
            # Artifacts need not exist before the first build.
            destination = (path.parent / target.split('#')[0]).resolve()
            if not dist and destination.parent == ROOT / 'dist':
                continue
            assert destination.exists(), f'Broken link: {path}: {target}'
            links += 1
        assert not re.search(r'-----BEGIN .*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}', text), f'Secret pattern: {path}'
    values = calculate()
    targets = {'cell_area_nm2': 1753.7014, 'density_per_um2': 570.2225,
               'gap_nm': 17, 'capacitance_fF': 8.565848, 'tip_deflection_nm': 12.124323,
               'residual_capacitance_ratio': 0.92, 'serial_clearance_min': 10.552381,
               'expected_cell_defects': 17.179869184, 'accepted_wafer_cost_usd': 12.24489796}
    for key, expected in targets.items():
        assert math.isclose(values[key], expected, rel_tol=0.001), f'Numerical mismatch: {key}: {values[key]}'
    if dist:
        manifest = json.loads((ROOT / 'dist/manifest.json').read_text())
        assert manifest['version'] == (ROOT / 'VERSION').read_text().strip()
        assert len(manifest['sources']) == 27
        for name, digest in manifest['sources'].items():
            assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, f'Stale build: {name}'
        for artifact in ('html', 'md'):
            source = (ROOT / f'dist/dram-sacrificial-capacitor-mold-removal.{artifact}').read_text()
            parser = Links()
            parser.feed(source)
            assert len(parser.ids) == len(set(parser.ids)), 'Duplicate anchors'
            hrefs = parser.hrefs if artifact == 'html' else re.findall(r'\]\((#[^)]+)\)', source)
            for href in hrefs:
                if href.startswith('#'):
                    assert href[1:] in parser.ids, f'Broken compiled anchor: {href}'
            assert len(parser.ids) == 27
    print(f'PASS: 16 chapters, 7 appendices, {links} local links, {len(targets)} numerical checks' + (', compiled anchors and source hashes' if dist else ''))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dist', action='store_true')
    validate(parser.parse_args().dist)
