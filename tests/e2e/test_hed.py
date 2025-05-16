from pages.form_page import FormPage
from pages.result_page import ResultPage

def test_uploading_imgs(page, hed_config):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto(hed_config["url"])
    form_page.upload_files(hed_config["img_path"])
    form_page.submit()
    
    assert result_page.get_stock_img() is True
    assert result_page.get_edges_img() is True


def test_noised_imgs(page, hed_config):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto(hed_config["url"])
    form_page.use_bsds500()
    form_page.add_noise('impulse', str(0.03))
    form_page.submit()
    
    assert result_page.get_stock_img() is True
    assert result_page.get_edges_img() is True


def test_calculate_metrics(page, hed_config):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto(hed_config["url"])
    form_page.use_bsds500()
    form_page.get_metrics()
    form_page.submit()
    
    assert result_page.get_stock_img() is True
    assert result_page.get_edges_img() is True
    assert result_page.get_metrics() is True

def test_gt_uploading(page, hed_config):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto(hed_config["url"])
    form_page.upload_files(hed_config["img_path"])
    form_page.get_metrics()
    form_page.upload_gt(hed_config["gt_path"])
    form_page.submit()
    
    assert result_page.get_stock_img() is True
    assert result_page.get_edges_img() is True
    assert result_page.get_metrics() is True


