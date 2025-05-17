import pytest

@pytest.fixture(scope="session")
def config():
    return {
            "url": "https://devedges.pythonanywhere.com",
            "noise_type": "impulse",
            "correct_value": 0.03,
            "incorrect_value": 100,
            "img_path": "./bsds500/imgs/",
            "gt_path": "./bsds500/gts/",
            "many_files_path":"./tests/files/",
            "large_file_path":"./tests/files/large_file.jpg"
        }