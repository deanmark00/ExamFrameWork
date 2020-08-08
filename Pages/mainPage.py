class MainPage():

    def __init__(self, driver):
        self.driver = driver

        self.account_button_id = "navbarAccount"
        self.accountLogin_button_id = "navbarLoginButton"
        self.accountLogout_button_id = "navbarLogoutButton"
        self.yourBasket_button_xpath ="//body//button[4]"
        self.buyAppleJuice_button_xpath = "//mat-grid-tile[1]//figure[1]//mat-card[1]//div[3]//button[1]"
        self.buyApplePomace_button_xpath = "//mat-grid-tile[2]//figure[1]//mat-card[1]//div[3]//button[1]"
        self.buyBananaJuice_button_xpath = "//mat-grid-tile[3]//figure[1]//mat-card[1]//div[3]//button[1]"
        self.buyCarrotJuice_button_xpath = "//mat-grid-tile[4]//figure[1]//mat-card[1]//div[3]//button[1]"
        self.buyEggfruiJuice_button_xpath = "//mat-grid-tile[5]//figure[1]//mat-card[1]//div[2]//button[1]"
        self.buyFruitPress_button_xpath = "//mat-grid-tile[6]//figure[1]//mat-card[1]//div[2]//button[1]"
        self.buyGreenSmoothie_button_xpath = "//mat-grid-tile[7]//figure[1]//mat-card[1]//div[3]//button[1]"
        self.buyCommonTradingCard_button_xpath = "//mat-grid-tile[8]//figure[1]//mat-card[1]//div[2]//button[1]"
        self.buySuperRareTradingCard_button_xpath = "//mat-grid-tile[9]//figure[1]//mat-card[1]//div[3]//button[1]"
        self.buyJuiceShopArtwork_button_xpath = "//mat-grid-tile[10]//figure[1]//mat-card[1]//div[3]//button[1]"
        self.buyLemonJuice_button_xpath = "//mat-grid-tile[11]//figure[1]//mat-card[1]//div[2]//button[1]"
        self.buyMelonBike_button_xpath = "//mat-grid-tile[12]//figure[1]//mat-card[1]//div[3]//button[1]"

    def account_button(self):
        self.driver.find_element_by_id(self.account_button_id).click()

    def account_login(self):
        self.driver.find_element_by_id(self.accountLogin_button_id).click()

    def account_logout(self):
        self.driver.find_element_by_id(self.accountLogout_button_id).click()

    def your_basket(self):
        self.driver.find_element_by_xpath(self.yourBasket_button_xpath).click()

    def buy_apple_juice(self):
        self.driver.find_element_by_xpath(self.buyAppleJuice_button_xpath).click()

    def buy_apple_juicepomace(self):
        self.driver.find_element_by_xpath(self.buyApplePomace_button_xpath).click()

    def buy_banana_juice(self):
        self.driver.find_element_by_xpath(self.buyBananaJuice_button_xpath).click()

    def buy_carrot_juice(self):
        self.driver.find_element_by_xpath(self.buyCarrotJuice_button_xpath).click()

    def buy_eggfruit_juice(self):
        self.driver.find_element_by_xpath(self.buyEggfruiJuice_button_xpath).click()

    def buy_fruit_press(self):
        self.driver.find_element_by_xpath(self.buyFruitPress_button_xpath).click()

    def buy_green_smoothie(self):
        self.driver.find_element_by_xpath(self.buyGreenSmoothie_button_xpath).click()

    def buy_common_trading_card(self):
        self.driver.find_element_by_xpath(self.buyCommonTradingCard_button_xpath).click()

    def buy_super_rare_trading_card(self):
        self.driver.find_element_by_xpath(self.buySuperRareTradingCard_button_xpath).click()

    def buy_juice_shop_artwork(self):
        self.driver.find_element_by_xpath(self.buyJuiceShopArtwork_button_xpath).click()

    def buy_lemon_juice(self):
        self.driver.find_element_by_xpath(self.buyLemonJuice_button_xpath).click()

    def buy_melon_bike(self):
        self.driver.find_element_by_xpath(self.buyMelonBike_button_xpath).click()








