"""Reproduce declared teaching models; no external data or credentials."""
import json
import math


def calculate():
    pitch, diameter, height = 45.0, 28.0, 1600.0
    cell_area = math.sqrt(3) * pitch**2 / 2
    exposed_height = height - 120 - 50 - 20
    area = math.pi * diameter * exposed_height * 1e-18
    moment = math.pi * (diameter * 1e-9)**4 / 64
    return {
        'cell_area_nm2': cell_area,
        'density_per_um2': 1e6 / cell_area,
        'density_at_42nm_per_um2': 1e6 / (math.sqrt(3) * 42**2 / 2),
        'gap_nm': pitch - diameter,
        'oxide_equivalent_thickness_nm': 1410 * (1 - math.pi * diameter**2 / (4 * cell_area)),
        'opening_fraction': math.pi * 25**2 / (math.sqrt(3) * 90**2 / 2),
        'planar_farthest_distance_nm': 90 / math.sqrt(3) - 25,
        'exposed_area_um2': area * 1e12,
        'capacitance_fF': 8.8541878128e-12 * 3.9 * area / (0.5e-9) * 1e15,
        'residual_capacitance_ratio': 0.9 + 0.1 * 0.5 / 2.5,
        'serial_clearance_min': 650 / 70 + 760 / 600,
        'short_serial_clearance_min': 100 / 70 + 760 / 600,
        'diffusion_time_s': (0.8e-6)**2 / 1e-9,
        'moment_m4': moment,
        'tip_deflection_nm': 1e-9 * (760e-9)**3 / (3 * 400e9 * moment) * 1e9,
        'pressure_scale_MPa': 2 * 0.072 / (17e-9) / 1e6,
        'section_stress_multiplier': 1000 / (46.5 * 16),
        'support_remaining_nm': 50 - 2 * 1 * 1.75,
        'revised_stop_limit_min': 2 / 1.2,
        'five_exchange_fraction': math.exp(-5),
        'zero_event_bound_1million': -math.log(0.05) / 1e6,
        'zero_event_trials_for_1ppb': -math.log(0.05) / 1e-9,
        'expected_cell_defects': 2**34 * 1e-9,
        'unrepaired_zero_event_probability': math.exp(-2**34 * 1e-9),
        'accepted_wafer_cost_usd': (600 / 60 + 2) / 0.98,
        'alternative_break_even_baseline_yield': 12 / (14 / 0.995),
    }


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2, sort_keys=True))
