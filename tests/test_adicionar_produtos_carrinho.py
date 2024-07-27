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

#adc produto 1
btn_add_product = browser.find_element(By.XPATH, "//*[@id= 'add-to-cart-sauce-labs-bike-light']");
btn_add_product.click();

#Acessando Carrinho
browser.find_element(By.XPATH, "//*[@class = 'shopping_cart_link']").click();

#Voltando para tela de produtos
browser.find_element(By.ID, "continue-shopping").click();

#adc produto 2
browser.find_element(By.XPATH, "//*[@id= 'add-to-cart-sauce-labs-onesie']").click();

#Acessando Carrinho
browser.find_element(By.XPATH, "//*[@class = 'shopping_cart_link']").click();

time.sleep(5)