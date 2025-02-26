import os
import json

from MUSEpack.MUSEpack.MUSEreduce import musereduce

root_dir = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(root_dir, 'data')
data_dir1 = data_dir + "/"

raw_dir = os.path.join(data_dir, 'raw', 'NGC1856_CENTER_P01')
calib_dir = os.path.join(data_dir, 'calibration')    # calibration exposures (bias, dark, flat, etc.)
reduced_dir = os.path.join(data_dir, 'reduced')     # Intermediate output directory for pixel tables and reduced cubes
output_dir = os.path.join(data_dir, 'output')  # Final output

# Test configuration

config = {
    "raw_directory": raw_dir,
    "calibration_directory": calib_dir,
    "reduced_directory": reduced_dir,
    "output_directory": output_dir,
    "global": {
        "withrvcorr": True,
        "OB_list": ["NGC1856_CENTER_P01"],
        "OB": "NGC1856_CENTER_P01",
        "dither_multiple_OBs": False,
        "rootpath": data_dir1,
        "mode": "WFM",
        "auto_sort_data": True,
        "using_specific_exposure_time": False,
        "n_CPU": 4,  # Maybe adjust?
        "pipeline_path": "/home/linuxbrew/.linuxbrew/bin/esoreflex",
    },
    "calibration": {
        "using_ESO_calibration": False,
        "dark": True,
        "renew_statics": False,
        "execute": True,
        "create_sof": True,
    },
    "sci_basic": {
        "skyreject": True,
        "skylines": "5577.339,6300.304",
        "execute_std": True,
        "execute": True,
        "create_sof": True,
    },
    "sky": {
        "sky_field": False,
        "fraction": 0.2,
        "ignore": False,
        "method": "model",
        "execute": True,
        "create_sof": True,
        "modified": True,
    },
    "std_flux": {
        "execute": True,
        "create_sof": True,
    },
    "sci_post": {
        "subtract_sky": True,
        "autocalib": True,
        "raman": False,
        "execute": True,
        "create_sof": True,
    },
    "exp_combine": {
        "weight": "exptime",
        "execute": True,
        "create_sof": True,
    },
    "dither_collect": {
        "user_list": [],
        "execute": True,
    },
    "exp_align": {
        "execute": True,
        "create_sof": True
    },
    "reduction": {
        "bias": True,
        "dark": True,
        "flat": True,
        "wavelength_calibration": True,
        "illumination_flat": True,
        # For sky subtraction, use the modified method to better handle crowded fields:
        "sky_subtraction": {
            "modified": True,
            "method": "subtract-model",
            "sky_fraction": 0.2  # Fraction of the field assumed to be sky dominated - check if this is apt
        },
        "flux_calibration": True,
        "telluric_correction": True,
        "astrometric_correction": True
    },
    "cube": {
        "wavelength_range": [4600, 9350],
        "spatial_sampling": 0.2,           # arcsec per pixel
        "drizzle": True                    # drizzle-like resampling to conserve flux
    }
}

# config to json - pipeline wrapper requirement

config_file = os.path.join(reduced_dir, "config.json")
with open(config_file, "w") as f:
    json.dump(config, f, indent=4)

print("Configuration file written to:", config_file)

# Basic Reduction

reducer = musereduce(configfile=config_file)
reducer.execute()
