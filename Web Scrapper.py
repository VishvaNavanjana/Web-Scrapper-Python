import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Path to chromedriver.exe
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')
driver.get("https://oxylabs.io/blog")

results = []