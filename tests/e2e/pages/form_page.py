import os

class FormPage:
    def __init__(self, page):
        self.page = page
        self.page.on("dialog", self._handle_dialog)

    def _handle_dialog(self, dialog):
        print(f"[ALERT] {dialog.message}")

    def goto(self, url: str):
        print("→ Navigating to page...")
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')

    def upload_files(self, folder_path: str):
        print("↑ Uploading input images...")
        file_paths = self._get_files(folder_path)
        self.page.wait_for_selector('[data-testid="fileUpload"]')
        self.page.set_input_files('[data-testid="fileUpload"]', file_paths)

    def upload_gt(self, folder_path: str):
        print("↑ Uploading ground truth images...")
        file_paths = self._get_files(folder_path)
        self.page.wait_for_selector('[data-testid="upload_gt"]')
        self.page.set_input_files('[data-testid="upload_gt"]', file_paths)

    def use_bsds500(self):
        print("✓ Using BSDS500 preset")
        self.page.click('[data-testid="use_bsds500"]')

    def add_noise(self, noise_type: str, value: any):
        print(f"+ Adding noise: {noise_type} = {value}")
        self.page.click('[data-testid="noise_check"]')
        self.page.select_option('[data-testid="noise_type"]', noise_type)
        self.page.fill('[data-testid="noise_value"]', str(value))

    def get_metrics(self):
        print("✓ Enabling metrics collection")
        self.page.click('[data-testid="metrics_checkbox"]')

    def submit(self):
        print("→ Submitting form")
        self.page.click('[data-testid="submit_btn"]', no_wait_after=True)

    @staticmethod
    def _get_files(path: str) -> list[str]:
        abs_path = os.path.abspath(path)

        if os.path.isfile(abs_path):
            return [abs_path]

        return [
            os.path.join(abs_path, f)
            for f in os.listdir(abs_path)
            if os.path.isfile(os.path.join(abs_path, f))
        ]
