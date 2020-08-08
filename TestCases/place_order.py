from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "......", "......"))
from Pages.loginPage import LoginPage
from Pages.mainPage import MainPage
from Pages.placeOrder import PlaceOrder
from Pages.selectAddress import SelectAddress
from Pages.deliverySpeed import DeliverySpeed
from Pages.paymentOptions import PaymentOptions
import HtmlTestRunner


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = "C:/Users/denma/PycharmProjects/ExamFrameWork/drivers/chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_one_day_order(self):
        driver = self.driver
        mainpage = MainPage(driver)
        placerorder = PlaceOrder(driver)
        address = SelectAddress(driver)
        delivery = DeliverySpeed(driver)
        payment = PaymentOptions(driver)
        self.driver.get("http://139.99.96.214:3000/#/search")
        self.driver.find_element_by_xpath("//body//mat-dialog-container//button[2]").click()
        mainpage.account_button()
        mainpage.account_login()
        login = LoginPage(driver)
        login.enter_email("test@test.com")
        login.enter_password("abcd1234")
        login.click_login()
        mainpage.buy_eggfruit_juice()
        time.sleep(3)
        mainpage.your_basket()
        time.sleep(3)
        placerorder.checkout_button()
        time.sleep(3)
        address.first_address()
        time.sleep(3)
        address.continue_button()
        time.sleep(3)
        delivery.one_day_delivery()
        time.sleep(3)
        delivery.continue_button()
        time.sleep(3)
        payment.first_card()
        time.sleep(3)
        payment.continue_button()
        time.sleep(3)
        self.driver.find_element_by_id("checkoutButton").click()
        self.driver.save_screenshot("C:/Users/denma/PycharmProjects/ExamFrameWork/Screenshots" + "test_one_day_order.png")

    def test_fast_delivery(self):
        driver = self.driver
        mainpage = MainPage(driver)
        placerorder = PlaceOrder(driver)
        address = SelectAddress(driver)
        delivery = DeliverySpeed(driver)
        payment = PaymentOptions(driver)
        self.driver.get("http://139.99.96.214:3000/#/search")
        self.driver.find_element_by_xpath("//body//mat-dialog-container//button[2]").click()
        mainpage.account_button()
        mainpage.account_login()
        login = LoginPage(driver)
        login.enter_email("test@test.com")
        login.enter_password("abcd1234")
        login.click_login()
        mainpage.buy_eggfruit_juice()
        time.sleep(3)
        mainpage.your_basket()
        time.sleep(3)
        placerorder.checkout_button()
        time.sleep(3)
        address.first_address()
        time.sleep(3)
        address.continue_button()
        time.sleep(3)
        delivery.fast_delivery()
        time.sleep(3)
        delivery.continue_button()
        time.sleep(3)
        payment.first_card()
        time.sleep(3)
        payment.continue_button()
        time.sleep(3)
        self.driver.find_element_by_id("checkoutButton").click()
        self.driver.save_screenshot("C:/Users/denma/PycharmProjects/ExamFrameWork/Screenshots" + "test_fast_delivery.png")


    def test_standard_order(self):
        driver = self.driver
        mainpage = MainPage(driver)
        placerorder = PlaceOrder(driver)
        address = SelectAddress(driver)
        delivery = DeliverySpeed(driver)
        payment = PaymentOptions(driver)
        self.driver.get("http://139.99.96.214:3000/#/search")
        self.driver.find_element_by_xpath("//body//mat-dialog-container//button[2]").click()
        mainpage.account_button()
        mainpage.account_login()
        login = LoginPage(driver)
        login.enter_email("test@test.com")
        login.enter_password("abcd1234")
        login.click_login()
        mainpage.buy_eggfruit_juice()
        time.sleep(3)
        mainpage.your_basket()
        time.sleep(3)
        placerorder.checkout_button()
        time.sleep(3)
        address.first_address()
        time.sleep(3)
        address.continue_button()
        time.sleep(3)
        delivery.standard_delivery()
        time.sleep(3)
        delivery.continue_button()
        time.sleep(3)
        payment.first_card()
        time.sleep(3)
        payment.continue_button()
        time.sleep(3)
        self.driver.find_element_by_id("checkoutButton").click()
        self.driver.save_screenshot("C:/Users/denma/PycharmProjects/ExamFrameWork/Screenshots" + "test_standard_order.png")


    def test_pay_wallet(self):
        driver = self.driver
        mainpage = MainPage(driver)
        placerorder = PlaceOrder(driver)
        address = SelectAddress(driver)
        delivery = DeliverySpeed(driver)
        payment = PaymentOptions(driver)
        self.driver.get("http://139.99.96.214:3000/#/search")
        self.driver.find_element_by_xpath("//body//mat-dialog-container//button[2]").click()
        mainpage.account_button()
        mainpage.account_login()
        login = LoginPage(driver)
        login.enter_email("test@test.com")
        login.enter_password("abcd1234")
        login.click_login()
        mainpage.buy_eggfruit_juice()
        time.sleep(2)
        mainpage.your_basket()
        time.sleep(2)
        placerorder.checkout_button()
        time.sleep(2)
        address.first_address()
        time.sleep(2)
        address.continue_button()
        time.sleep(2)
        delivery.standard_delivery()
        time.sleep(2)
        delivery.continue_button()
        time.sleep(2)
        payment.pay_using_wallet()
        time.sleep(2)
        self.driver.find_element_by_id("checkoutButton").click()
        self.driver.save_screenshot("C:/Users/denma/PycharmProjects/ExamFrameWork/Screenshots" + "test_pay_wallet.png")


    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
        print("Test Complete")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/denma/PycharmProjects/ExamFrameWork/Reports'))