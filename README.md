# ExamFrameWork
 
I apologize since this is my first time writing codes and creating a framework.

How to run the test:

1. Import the directories needed

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

2. Create test class and user unittest

3. Create a setUp for any executables that are always needed to be executed like getting windows and maximizing it

4. Create test cases

5. Use the directories from the created Page Object Models

6. Create tearDown for any executables after a test case like closing the driver and printing statements

7. Create a testRunner code for the html reports

8. Framework can be run through command prompt by going to the file folder project. Mine displays as 
"C:\Users\denma\PycharmProjects\ExamFrameWork>"
then type 
testing log in = python -m TestCases.test_login
testing placeing an order = python -m TestCases.place_order
