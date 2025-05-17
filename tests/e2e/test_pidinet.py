from pages.form_page import FormPage
from pages.result_page import ResultPage

page_url = "/pidinet"

def test_uploading_imgs(page, config):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto(config["url"]+page_url)
    form_page.upload_files(config["img_path"])
    form_page.submit()
    
    assert result_page.get_stock_img() is True
    assert result_page.get_edges_img() is True


def test_noised_imgs(page, config):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto(config["url"]+page_url)
    form_page.use_bsds500()
    form_page.add_noise('impulse', config["correct_value"])
    form_page.submit()
    
    assert result_page.get_stock_img() is True
    assert result_page.get_edges_img() is True


def test_calculate_metrics(page, config):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto(config["url"]+page_url)
    form_page.use_bsds500()
    form_page.get_metrics()
    form_page.submit()
    
    assert result_page.get_stock_img() is True
    assert result_page.get_edges_img() is True
    assert result_page.get_metrics() is True

def test_gt_uploading(page, config):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto(config["url"]+page_url)
    form_page.upload_files(config["img_path"])
    form_page.get_metrics()
    form_page.upload_gt(config["gt_path"])
    form_page.submit()
    
    assert result_page.get_stock_img() is True
    assert result_page.get_edges_img() is True
    assert result_page.get_metrics() is True

def test_upload_counter_validation(page, config):
    form_page = FormPage(page)

    alerts = []
    page.on("dialog", lambda dialog: (alerts.append(dialog.message), dialog.accept()))

    form_page.goto(config["url"]+page_url)
    form_page.upload_files(config["many_files_path"])
    form_page.submit()

    assert any("You can upload at most 10 images" in msg for msg in alerts)


def test_upload_size_validation(page, config):
    form_page = FormPage(page)

    alerts = []
    page.on("dialog", lambda dialog: (alerts.append(dialog.message), dialog.accept()))

    form_page.goto(config["url"]+page_url)
    form_page.upload_files(config["large_file_path"])
    form_page.submit()

    assert any("Image size should be less than 1 MB" in msg for msg in alerts)

def test_min_max_validation(page, config):
    form_page = FormPage(page)
    
    form_page.goto(config["url"]+page_url)
    form_page.upload_files(config["img_path"])
    form_page.add_noise('impulse', str(config["incorrect_value"]))

    form_page.submit()

    is_invalid = page.eval_on_selector('input[data-testid="noise_value"]', 'el => el.validity.rangeOverflow || el.validity.rangeUnderflow')
    assert is_invalid


def test_gt_upload_validation(page, config):
    form_page = FormPage(page)

    alerts = []
    page.on("dialog", lambda dialog: (alerts.append(dialog.message), dialog.accept()))

    form_page.goto(config["url"]+page_url)
    form_page.upload_files(config["img_path"])
    form_page.get_metrics()
    form_page.upload_gt(config["many_files_path"])
    form_page.submit()

    assert any("Number of original images must match number of ground truth images" in msg for msg in alerts)
    