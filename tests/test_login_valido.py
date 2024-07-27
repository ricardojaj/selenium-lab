import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome();
browser.get("https://www.saucedemo.com/");
browser.maximize_window();

username = browser.find_element(By.XPATH, "//*[@id='user-name']");
username.send_keys("standard_user");

password = browser.find_element(By.XPATH, "//*[@id= 'password']");
password.send_keys("secret_sauce");

btn_login = browser.find_element(By.XPATH, "//*[@id= 'login-button']");
btn_login.click();

products_title = browser.find_element(By.XPATH, "//span[@class='title']")
assert products_title.is_displayed();

time.sleep(5);