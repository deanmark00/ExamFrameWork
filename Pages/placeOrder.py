class PlaceOrder():

    def __init__(self, driver):
        self.driver = driver

        self.reduce_button_xpath = "//mat-cell[3]//button[1]"
        self.increase_button_xpath = "//body//app-basket//button[2]"
        self.delete_button_xpath = "//mat-cell[5]//button[1]"
        self.checkout_button_id = "checkoutButton"

    def reduce_button(self):
        self.driver.find_element_by_xpath(self.reduce_button_xpath).click()

    def increase_button(self):
        self.driver.find_element_by_xpath(self.increase_button_xpath).click()

    def delete_button(self):
        self.driver.find_element_by_xpath(self.delete_button_xpath).click()

    def checkout_button(self):
        self.driver.find_element_by_id(self.checkout_button_id).click()


