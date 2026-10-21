
"""Smart Home Garden Irrigation System."""

def check_soil_moisture(moisture, threshold=40):
    if moisture < threshold:
        return "Irrigation Required"
    return "Soil Moisture Sufficient"


def calculate_water_needed(moisture, target=60):
    if moisture >= target:
        return 0
    return target - moisture


def control_pump(moisture, threshold=40):
    if moisture < threshold:
        return "Pump ON"
    return "Pump OFF"
