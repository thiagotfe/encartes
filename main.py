from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import urllib.request

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.get("https://loja.centerbox.com.br/loja/58/encartes")

time.sleep(15)

imgs = driver.find_elements(By.CSS_SELECTOR, 'div.flip-card > div.card-body > img')

for i, img in enumerate(imgs):
	src = img.get_attribute('src')
	urllib.request.urlretrieve(src, f"img_{i+1}.png")

time.sleep(30)

driver.quit()