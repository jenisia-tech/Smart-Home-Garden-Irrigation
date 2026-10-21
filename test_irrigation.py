
"""Unit tests for the smart garden irrigation system."""

import unittest
from irrigation import (
    check_soil_moisture,
    calculate_water_needed,
    control_pump
)


class TestIrrigation(unittest.TestCase):

    def test_dry_soil(self):
        self.assertEqual(
            check_soil_moisture(25),
            "Irrigation Required"
        )

    def test_sufficient_moisture(self):
        self.assertEqual(
            check_soil_moisture(60),
            "Soil Moisture Sufficient"
        )

    def test_water_needed(self):
        self.assertEqual(calculate_water_needed(30), 30)

    def test_no_water_needed(self):
        self.assertEqual(calculate_water_needed(70), 0)

    def test_pump_on(self):
        self.assertEqual(control_pump(20), "Pump ON")

    def test_pump_off(self):
        self.assertEqual(control_pump(50), "Pump OFF")


if __name__ == "__main__":
    unittest.main()
