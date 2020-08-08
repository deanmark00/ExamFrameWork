class PaymentOptions():

    def __init__(self, driver):
        self.driver = driver

        self.firstCardOption_generic_xpath = "//mat-row[1]//mat-cell[1]//mat-radio-button[1]"
        self.secondCardOption_generic_xpath = "//mat-row[2]//mat-cell[1]//mat-radio-button[1]"
        self.addNewCard_button_id = "mat-expansion-panel-header-0"
        self.name_textbox_id = "mat-input-7"
        self.cardNumber_spinbutton_id = "mat-input-8"
        self.expiryMonth_combobox_id = "mat-input-9"
        self.expiryYear_combobox_id = "mat-input-10"
        self.payWallet_button_xpath = "//button[@class='mat-focus-indicator btn mat-raised-button mat-button-base mat-primary']"
        self.addCoupon_button_id = "mat-expansion-panel-header-1"
        self.coupon_textbox_id = "coupon"
        self.redeem_button_id = "applyCouponButton"
        self.otherPaymentOptions_button_id = "mat-expansion-panel-header-2"
        self.stripeCreditCard_button_xpath = "//div//div//div//div//div//div[1]//div[2]//a[1]//button[1]"
        self.spreadShirtUS_button_xpath = "//body//div[2]//div[2]//a[1]//button[1]"
        self.spreadShirtDE_button_xpath = "//a[2]//button[1]"
        self.stickerYou_button_xpath = "//a[3]//button[1]"
        self.leanPub_button_xpath = "//a[4]//button[1]"
        self.back_button_xpath = "//body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-payment/mat-card/div/div/button[1]"
        self.continue_button_xpath = "//body//app-payment//button[2]"

    def first_card(self):
        self.driver.find_element_by_xpath(self.firstCardOption_generic_xpath).click()

    def second_card(self):
        self.driver.find_element_by_xpath(self.secondCardOption_generic_xpath).click()

    def add_new_card(self):
        self.driver.find_element_by_id(self.addNewCard_button_id).click()

    def enter_card_name(self, crdname):
        self.driver.find_element_by_id(self.name_textbox_id).clear()
        self.driver.find_element_by_id(self.name_textbox_id).send_keys(crdname)

    def enter_card_number(self, crdnumber):
        self.driver.find_element_by_id(self.cardNumber_spinbutton_id).clear()
        self.driver.find_element_by_id(self.cardNumber_spinbutton_id).send_keys(crdnumber)

    def choose_expiry_month(self):
        self.driver.find_element_by_id(self.expiryMonth_combobox_id).click()

    def choose_expiry_year(self):
        self.driver.find_element_by_id(self.expiryYear_combobox_id).click()

    def pay_using_wallet(self):
        self.driver.find_element_by_xpath(self.payWallet_button_xpath).click()

    def add_coupon(self):
        self.driver.find_element_by_id(self.addCoupon_button_id).click()

    def enter_coupon_code(self, cpnnumber):
        self.driver.find_element_by_id(self.coupon_textbox_id).clear()
        self.driver.find_element_by_id(self.coupon_textbox_id).send_keys(cpnnumber)

    def redeem_button(self):
        self.driver.find_element_by_id(self.redeem_button_id).click()

    def other_payment_options(self):
        self.driver.find_element_by_id(self.otherPaymentOptions_button_id).click()

    def stripe_credit_card(self):
        self.driver.find_element_by_xpath(self.stripeCreditCard_button_xpath).click()

    def spread_shirt_us(self):
        self.driver.find_element_by_xpath(self.spreadShirtUS_button_xpath).click()

    def spread_shirt_de(self):
        self.driver.find_element_by_xpath(self.spreadShirtDE_button_xpath).click()

    def sticker_you(self):
        self.driver.find_element_by_xpath(self.stickerYou_button_xpath).click()

    def lean_pub(self):
        self.driver.find_element_by_xpath(self.leanPub_button_xpath).click()

    def back_button(self):
        self.driver.find_element_by_xpath(self.back_button_xpath).click()

    def continue_button(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()




















