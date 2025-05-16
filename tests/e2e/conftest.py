import pytest

@pytest.fixture(scope="session")
def config():
    return {
        "hed": {
            "url": "https://devedges.pythonanywhere.com/hed",
            "noise_type": "impulse",
            "correct_value": 0.03,
            "incorrect_value": 100,
            "img_path": "./bsds500/imgs/",
            "gt_path": "./bsds500/gts/",
        }
    }

@pytest.fixture
def hed_config(config):
    return config["hed"]