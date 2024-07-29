import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome();
browser.get("https://www.saucedemo.com/");
browser.maximize_window();

username = browser.find_element(By.XPATH, "//*[@id='user-name']");
username.send_keys("standard_user");

password = browser.find_element(By.XPATH, "//*[@id= 'password']");
password.send_keys("senhaInvalida");

btn_login = browser.find_element(By.XPATH, "//*[@id= 'login-button']");
btn_login.click();

msgSenhaInvalida = browser.find_element(By.XPATH, "//h3[@data-test='error']")
assert msgSenhaInvalida.text == 'Epic sadface: Username and password do not match any user in this service';

print(msgSenhaInvalida.text);
time.sleep(5);