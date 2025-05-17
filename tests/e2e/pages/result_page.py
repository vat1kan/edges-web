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

    def get_edges_comparison(self):
        cells = self.page.locator('[class="result-row"]')
        count = cells.count()

        for i in range(count):
            try:
                cell = cells.nth(i)
                cell.wait_for(state="visible", timeout=90000)

                hed_img = cell.locator('[data-testid="hed_edges"]')
                pidinet_img = cell.locator('[data-testid="pidinet_edges"]')

                hed_img.wait_for(state="visible", timeout=90000)
                pidinet_img.wait_for(state="visible", timeout=90000)

                hed_nw = hed_img.evaluate("img => img.naturalWidth")
                hed_nh = hed_img.evaluate("img => img.naturalHeight")
                pidinet_nw = pidinet_img.evaluate("img => img.naturalWidth")
                pidinet_nh = pidinet_img.evaluate("img => img.naturalHeight")

                if hed_nw == 0 or hed_nh == 0:
                    print(f"Cell {i}: hed_edges image not loaded properly")
                    return False
                if pidinet_nw == 0 or pidinet_nh == 0:
                    print(f"Cell {i}: pidinet_edges image not loaded properly")
                    return False

            except Exception as e:
                print(f"Error in cell {i}: {e}")
                return False

        return True
    
    def get_metrics_comparison(self):
        cells = self.page.locator('[class="result-row"]')
        count = cells.count()

        for i in range(count):
            try:
                cell = cells.nth(i)
                cell.wait_for(state="visible", timeout=90000)

                cell.locator('[data-testid="hed_metrics"]').wait_for(state="visible")
                cell.locator('[data-testid="pidinet_metrics"]').wait_for(state="visible")

            except Exception as e:
                print(f"Error in cell {i}: {e}")
                return False

        return True