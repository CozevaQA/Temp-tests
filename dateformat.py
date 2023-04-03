import datetime
from dateutil.relativedelta import relativedelta
import configparser
import os
import time
import traceback
from tkinter import *
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import variablestorage as locator
from openpyxl import Workbook, load_workbook
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException, TimeoutException


from openpyxl.styles import Font, PatternFill
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

DoS = datetime.datetime.now()
DoS = DoS.strftime("%m/%d/%Y")
print(DoS)

start_time = time.perf_counter()
end_time = int(start_time)+60
while True:
    print(int(end_time - time.perf_counter()))
    time.sleep(1)
    if int(end_time - time.perf_counter()) < 1:
        break