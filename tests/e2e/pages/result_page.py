class ResultPage:
    def __init__(self, page):
        self.page = page

    def get_stock_img(self):
        assert self.page.locator('[data-testid="stock_img"]').is_visible()

    def get_edges_img(self):
        assert self.page.locator('[data-testid="edges_image"]').is_visible()

    def get_metrics(self):
        assert self.page.locator('[data-testid="edges_metrics"]').is_visible()