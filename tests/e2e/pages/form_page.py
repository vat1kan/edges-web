class FormPage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def upload_files(self, files):
        self.page.set_input_files('[data-testid="fileUpload"]', [files])

    def use_bsds500(self):
        self.page.click('[data-testid="use_bsds500"]')

    def add_noise(self, type, value):
        self.page.click('[data-testid="noise_check"]')
        self.page.select_option('[data-testid="noise_type"]', type)
        self.page.fill('[data-testid="noise_value"]', value)

    def get_metrics(self):
        self.page.click('[data-testid="metrics_checkbox"]')

    def upload_gt(self, files):
        self.page.set_input_files('[data-testid="upload_gt""]', [files])

    def submit(self):
        self.page.click('[data-testid="submit_btn"]')