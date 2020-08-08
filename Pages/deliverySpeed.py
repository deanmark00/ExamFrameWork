class DeliverySpeed():

    def __init__(self, driver):
        self.driver = driver

        self.oneDayDelivery_generic_xpath = "//mat-row[1]//mat-cell[1]//mat-radio-button[1]"
        self.fastDelivery_generic_xpath = "//mat-row[2]//mat-cell[1]//mat-radio-button[1]"
        self.standardDelivery_generic_xpath = "//mat-row[3]//mat-cell[1]//mat-radio-button[1]"
        self.back_button_xpath = "//body//app-delivery-method//button[1]"
        self.continue_button_xpath = "//body//app-delivery-method//button[2]"

    def one_day_delivery(self):
        self.driver.find_element_by_xpath(self.oneDayDelivery_generic_xpath).click()

    def fast_delivery(self):
        self.driver.find_element_by_xpath(self.fastDelivery_generic_xpath).click()

    def standard_delivery(self):
        self.driver.find_element_by_xpath(self.standardDelivery_generic_xpath).click()

    def back_button(self):
        self.driver.find_element_by_xpath(self.back_button_xpath).click()

    def continue_button(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()






