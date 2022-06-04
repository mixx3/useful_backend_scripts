import selenium.common.exceptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def proudly_recieve_chrome_driver():
	try:
		return webdriver.Chrome()
	except selenium.common.exceptions.WebDriverException:
		s = Service(ChromeDriverManager().install())
		return webdriver.Chrome(service=s)
