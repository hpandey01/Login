from selenium import webdriver
import os
import subprocess
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sys import argv
from tkinter import *

timeout=100
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://detectportal.firefox.com")

if driver.title=="Firewall Authentication":
	element_present = EC.presence_of_element_located((By.NAME, 'username'))
	WebDriverWait(driver, timeout).until(element_present)
	elem = driver.find_element_by_name("username")
	elem.clear()
	elem.send_keys(argv[1])
	elem = driver.find_element_by_name("password")
	elem.clear()
	elem.send_keys(argv[2])
	elem.submit()
time.sleep(2)

driver.execute_script('''window.open("http://nwm.iitk.ac.in","_blank");''')
driver.switch_to.window(driver.window_handles[1])
element_present = EC.presence_of_element_located((By.ID, 'rcmloginuser'))
WebDriverWait(driver, timeout).until(element_present)
elem = driver.find_element_by_id("rcmloginuser")
elem.clear()
elem.send_keys(argv[1])
elem = driver.find_element_by_id("rcmloginpwd")
elem.clear()
elem.send_keys(argv[2])
elem.submit()

driver.switch_to.window(driver.window_handles[0])
if driver.title!="Firewall Authentication Keepalive Window":
	driver.close()

driver.switch_to.window(driver.window_handles[-1])