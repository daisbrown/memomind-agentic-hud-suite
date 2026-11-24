"""Threshold checks for caller supplied readings, not a medical or vehicle safety system."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Alert:
    field: str
    value: float
    message: str


def check_readings(readings, limits=None):
    limits = limits or {'rear_psi_min': 30, 'front_psi_min': 30, 'coolant_c_max': 115, 'voltage_min': 11.5, 'fuel_range_mi_min': 20}
    rules = [('rear_psi', 'rear_psi_min', 'low'), ('front_psi', 'front_psi_min', 'low'), ('coolant_c', 'coolant_c_max', 'high'), ('voltage', 'voltage_min', 'low'), ('fuel_range_mi', 'fuel_range_mi_min', 'low')]
    alerts = []
    for field, limit, direction in rules:
        value = readings.get(field)
        if value is None: continue
        if (direction == 'low' and value < limits[limit]) or (direction == 'high' and value > limits[limit]):
            alerts.append(Alert(field, value, f'{field.upper()} {direction.upper()}'))
    return alerts
