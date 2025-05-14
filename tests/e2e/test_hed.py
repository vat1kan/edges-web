from pages.form_page import FormPage
from pages.result_page import ResultPage

def uploading_imgs(page):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto('/hed')
    form_page.upload_files('../../bsds500/imgs/1.jpg')
    form_page.submit()
    
    assert result_page.get_stock_img() == True
    assert result_page.get_edges_img() == True


def noised_imgs(page):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto('/hed')
    form_page.use_bsds500()
    form_page.add_noise('impulse',0.03)
    form_page.submit()
    
    assert result_page.get_stock_img() == True
    assert result_page.get_edges_img() == True


def calculate_metrics(page):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto('/hed')
    form_page.use_bsds500()
    form_page.get_metrics()
    form_page.submit()
    
    assert result_page.get_stock_img() == True
    assert result_page.get_edges_img() == True
    assert result_page.get_metrics() == True

def gt_uploading(page):

    form_page = FormPage(page)
    result_page = ResultPage(page)
    
    form_page.goto('/hed')
    form_page.upload_files('../../bsds500/imgs/1.jpg')
    form_page.get_metrics()
    form_page.upload_gt('../.../bsds500/gts/gt1.jpg')
    form_page.submit()
    
    assert result_page.get_stock_img() == True
    assert result_page.get_edges_img() == True
    assert result_page.get_metrics() == True


