"""Compile the ordered Markdown source into portable Markdown and HTML."""
from pathlib import Path
import hashlib
import json
import re
import markdown

ROOT = Path(__file__).resolve().parents[1]
STEM = 'dram-sacrificial-capacitor-mold-removal'


def sources():
    return [ROOT / 'PREFACE.md', ROOT / 'INDEX.md',
            *sorted((ROOT / 'chapters').glob('*.md')),
            *sorted((ROOT / 'appendices').glob('*.md')),
            ROOT / 'GLOSSARY.md', ROOT / 'REFERENCES.md']


def anchor(path):
    return 'book-' + re.sub(r'[^a-z0-9]+', '-', path.relative_to(ROOT).as_posix().lower()).strip('-')


def compile_book():
    paths = sources()
    known = {path.resolve(): anchor(path) for path in paths}
    pieces = ['# DRAM Sacrificial Capacitor Mold Removal\n\n'
              'ChipFoundryServices Technical Series · First edition · 2026-10-05\n\n']
    for path in paths:
        def rewrite(match):
            label, target = match.groups()
            if target.startswith(('https://', 'http://', '#')):
                return match.group(0)
            destination = (path.parent / target).resolve()
            if destination in known:
                return f'[{label}](#{known[destination]})'
            raise ValueError(f'Unmapped book link: {path}: {target}')
        body = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', rewrite, path.read_text())
        pieces.append(f'<a id="{anchor(path)}"></a>\n\n{body}\n\n')
    combined = '\n'.join(pieces)
    content = markdown.markdown(combined, extensions=['tables', 'fenced_code'])
    document = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DRAM Sacrificial Capacitor Mold Removal</title>
<style>
:root{color-scheme:light}body{margin:0;background:#f4f3ef;color:#19242b;font:18px/1.7 Georgia,serif}
main{max-width:900px;margin:2rem auto;padding:3rem;background:white}h1,h2,h3{font-family:system-ui,sans-serif;line-height:1.25;color:#153d50}
h1{margin-top:3rem;border-bottom:2px solid #c7d8df;padding-bottom:.6rem}h2{margin-top:2rem}a{color:#075f88;text-underline-offset:.2em}
table{border-collapse:collapse;width:100%;font:15px/1.5 system-ui,sans-serif;display:block;overflow-x:auto;margin:1.5rem 0}
th,td{border:1px solid #cbd4d8;padding:.7rem;text-align:left}th{background:#eaf0f3}pre{overflow:auto;background:#eef2f4;padding:1rem;font-size:14px}
code{font-size:.88em}nav{font:16px system-ui,sans-serif}a[id]{scroll-margin-top:1rem}
@media(max-width:700px){main{margin:0;padding:1.2rem}body{font-size:17px}}
@media print{body{background:white;font-size:11pt}main{max-width:none;margin:0;padding:0}h1{break-before:page}table,pre{break-inside:avoid}a{color:inherit}}
</style></head><body><main>
<nav><a href="#book-index-md">Contents</a> · <a href="#book-references-md">References</a></nav>
''' + content + '\n</main></body></html>\n'
    out = ROOT / 'dist'
    out.mkdir(exist_ok=True)
    (out / f'{STEM}.md').write_text(combined)
    (out / f'{STEM}.html').write_text(document)
    hashes = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    (out / 'manifest.json').write_text(json.dumps({'version': (ROOT / 'VERSION').read_text().strip(), 'sources': hashes}, indent=2) + '\n')
    print(f'Built {len(paths)} source documents into HTML and Markdown ({len(combined.split())} words).')


if __name__ == '__main__':
    compile_book()
