class ResultPage:
    def __init__(self, page):
        self.page = page

    def get_stock_img(self):
        self.page.locator('[data-testid="stock_img"]').first.wait_for(state="visible", timeout=90000)

        locators = self.page.locator('[data-testid="stock_img"]')
        count = locators.count()
    
        for i in range(count):
            try:
                locators.nth(i).wait_for(state="visible", timeout=90000)
            except Exception as e:
                print(f"Image {i} not visible: {e}")
                return False
        return True

    def get_edges_img(self):
        self.page.locator('[data-testid="edges_image"]').first.wait_for(state="visible", timeout=90000)

        locators = self.page.locator('[data-testid="edges_image"]')
        count = locators.count()
    
        for i in range(count):
            try:
                locators.nth(i).wait_for(state="visible", timeout=90000)
            except Exception as e:
                print(f"Image {i} not visible: {e}")
                return False
        return True

    def get_metrics(self):
        self.page.locator('[data-testid="edges_metrics"]').first.wait_for(state="visible", timeout=90000)

        locators = self.page.locator('[data-testid="edges_metrics"]')
        count = locators.count()
    
        for i in range(count):
            try:
                locators.nth(i).wait_for(state="visible", timeout=90000)
            except Exception as e:
                print(f"Image {i} not visible: {e}")
                return False
        return True
