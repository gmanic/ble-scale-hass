"""Constants for the BLE Scale integration."""
from __future__ import annotations

from enum import Enum

CONF_SCALE_MODEL = "scale_model"

# Supported scale models from ble-scale-sync
SCALE_MODELS = [
    "auto",
    "xiaomi_scale_2",
    "xiaomi_body_composition_scale",
    "xiaomi_scale_pro",
    "renpho_scale",
    "eufy_scale",
    "yunmai_mini",
    "yunmai_m8",
    "beurer_bf_800",
    "beurer_bf_900",
    "sanitas_sfb_912",
    "medisana_bs_445",
    "withings_body_scale",
    "nokia_body_scale",
    "fitbit_aria",
    "fitbit_aria_2",
    "garmin_index",
    "honor_scale",
    "realme_scale",
    "tefal_scale",
    "umami_scale",
    "haeno_scale",
    "picooc_scale",
]

# Metric units and attributes
METRIC_UNITS = {
    "weight": "kg",
    "fat_percentage": "%",
    "muscle_mass": "kg",
    "water_percentage": "%",
    "bone_mass": "kg",
    "basal_metabolism": "kcal",
    "bmi": None,
}

METRIC_ICONS = {
    "weight": "mdi:scale-bathroom",
    "fat_percentage": "mdi:percent",
    "muscle_mass": "mdi:dumbbell",
    "water_percentage": "mdi:water-percent",
    "bone_mass": "mdi:bone",
    "basal_metabolism": "mdi:fire",
    "bmi": "mdi:calculator",
}
