class SelectAddress():

    def __init__(self, driver):
        self.driver = driver

        self.firstAddress_button_xpath = "//mat-row[1]//mat-cell[1]//mat-radio-button[1]"
        self.secondAddress_button_xpath = "//mat-row[2]//mat-cell[1]//mat-radio-button[1]"
        self.thirdAddress_button_xpath = "//mat-row[3]//mat-cell[1]//mat-radio-button[1]"
        self.continue_button_xpath = "//body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-select/div[@id='card']/app-address/mat-card/button[1]"
        self.newAddress_button_xpath = "//div[@id='card']//app-address//mat-card//div//button"

    def first_address(self):
        self.driver.find_element_by_xpath(self.firstAddress_button_xpath).click()

    def second_address(self):
        self.driver.find_element_by_xpath(self.secondAddress_button_xpath).click()

    def third_address(self):
        self.driver.find_element_by_xpath(self.thirdAddress_button_xpath).click()

    def continue_button(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()

    def new_address_button(self):
        self.driver.find_element_by_xpath(self.newAddress_button_xpath).click()


