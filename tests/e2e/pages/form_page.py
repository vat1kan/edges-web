import os

class FormPage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        print("goto")
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')

    def upload_files(self, path):
        print("files uploading")
        files_path = os.path.abspath(path)
        self.page.wait_for_selector('[data-testid="fileUpload"]')
        self.page.set_input_files('[data-testid="fileUpload"]', read_files(files_path))

    def use_bsds500(self):
        print("using bsds500")
        self.page.click('[data-testid="use_bsds500"]')

    def add_noise(self, type, value):
        print("add noise")
        self.page.click('[data-testid="noise_check"]')
        self.page.select_option('[data-testid="noise_type"]', type)
        self.page.fill('[data-testid="noise_value"]', value)

    def get_metrics(self):
        print("get metrics")
        self.page.click('[data-testid="metrics_checkbox"]')

    def upload_gt(self, path):
        print("upload gt")
        gts_path = os.path.abspath(path)
        self.page.wait_for_selector('[data-testid="upload_gt"]')
        self.page.set_input_files('[data-testid="upload_gt"]', read_files(gts_path))

    def submit(self):
        print("Clicking submit")
        self.page.click('[data-testid="submit_btn"]', no_wait_after=True)

def read_files(folder_path):
    return [
        os.path.abspath(os.path.join(folder_path, f))
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]