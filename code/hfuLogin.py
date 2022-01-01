#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#for explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

def getUrl(myRoom, myUsername, myPassword, myName, geckoLogPath='./geckodriver.log', webdriverPath='.', timeout=15):

	try:
		opts = Options()
		opts.headless = True
		browser = webdriver.Firefox(service_log_path=geckoLogPath, options=opts)
		browser.set_window_size(1440, 900)
		#for debugging:
		#browser = webdriver.Firefox(service_log_path=geckoLogPath)

		browser.get('https://rooms.hs-furtwangen.de/rooms/'+myRoom)
		
		username= WebDriverWait(browser, timeout).until(
		EC.element_to_be_clickable((By.ID, "username"))
		)
		
		password= WebDriverWait(browser, timeout).until(
		EC.element_to_be_clickable((By.ID, "password"))
		)
		
		doNotCache= WebDriverWait(browser, timeout).until(
		EC.element_to_be_clickable((By.ID, "donotcache"))
		)
		
		signIn= WebDriverWait(browser, timeout).until(
		EC.element_to_be_clickable((By.NAME, "_eventId_proceed"))
		)

		username.click()
		username.send_keys(myUsername)
		password.click()
		password.send_keys(myPassword)
		doNotCache.click()
		signIn.click()

		#alfaview Website

		username2= WebDriverWait(browser, timeout).until(
		EC.element_to_be_clickable((By.NAME, "displayName"))
		)

		username2.click()
		username2.send_keys(myName)
		username2.send_keys(Keys.ENTER)

		acceptEULA= WebDriverWait(browser, timeout).until(
		EC.element_to_be_clickable((By.CLASS_NAME, "v-input--selection-controls__input"))
		)
		
		acceptEULA.click()
		
		openAlfaview= WebDriverWait(browser, timeout).until(
		EC.presence_of_element_located((By.CLASS_NAME, "button-min-width-x-large"))
		)
		url= openAlfaview.get_attribute('href')

		return url
		
	finally:
		try:
			browser.close()
		except:
			pass
