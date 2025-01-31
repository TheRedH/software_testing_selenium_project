import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def test_login(username, password):
    driver.execute_script("window.scrollBy(0, 300);")
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()


def test_add_car(car, city, color, price, image, motor, mile, fuel):
    target_link = driver.find_element(By.XPATH, "/html/body/div[3]/ul/li[7]/a")
    target_link.click()
    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(0.5)
    carname_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#menu7 > div > div > div > div > form > div:nth-child(2) > input")))
    carname_field.send_keys(car)
    time.sleep(0.5)
    city_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#menu7 > div > div > div > div > form > div:nth-child(3) > input")))
    city_field.send_keys(city)
    time.sleep(0.5)
    color_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#menu7 > div > div > div > div > form > div:nth-child(4) > input")))
    color_field.send_keys(color)
    time.sleep(0.5)
    price_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#menu7 > div > div > div > div > form > div:nth-child(5) > input")))
    price_field.send_keys(price)
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(0.5)
    image_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#menu7 > div > div > div > div > form > div:nth-child(6) > input")))
    image_field.send_keys(image)
    time.sleep(0.5)
    motor_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#menu7 > div > div > div > div > form > div:nth-child(7) > input")))
    motor_field.send_keys(motor)
    time.sleep(0.5)
    mile_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#menu7 > div > div > div > div > form > div:nth-child(8) > input")))
    mile_field.send_keys(mile)
    time.sleep(0.5)
    fuel_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#menu7 > div > div > div > div > form > div:nth-child(9) > input")))
    fuel_field.send_keys(fuel)
    time.sleep(0.5)
    submit_button = driver.find_element(By.CSS_SELECTOR, "#menu7 > div > div > div > div > form > div.form-group.mb-0.clearfix > button")
    submit_button.click()


def test_delete_car():
    target_link = driver.find_element(By.XPATH, "/html/body/div[3]/ul/li[2]/a")
    target_link.click()
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(0.5)
    delete_button = driver.find_element(By.CSS_SELECTOR, "#menu2 > div > div:nth-child(1) > div > div.detail > a")
    delete_button.click()
    time.sleep(0.5)


def test_shopping_cart():
    target_link = driver.find_element(By.XPATH, "/html/body/div[3]/ul/li[4]/a")
    target_link.click()
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(0.5)
    confirm_button = driver.find_element(By.CSS_SELECTOR, "#menu4 > div.main-title.text-right > a.btn.btn-lg.btn-success")
    confirm_button.click()
    time.sleep(0.5)


def test_about_button():
    target_link = driver.find_element(By.CSS_SELECTOR, "#navbar > ul > li:nth-child(4) > a")
    target_link.click()
    time.sleep(0.5)


def test_question_session():
    driver.execute_script("window.scrollBy(0, 400);")
    target_link = driver.find_element(By.CSS_SELECTOR, "#menu1 > table > tbody > tr > td:nth-child(4) > a")
    target_link.click()
    time.sleep(0.5)

    
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 1)
driver.get('http://127.0.0.1:8000/accounts/dashboard')

print("TEST 1(LOGIN TEST): THE LOGIN TEST IS THE FIRST TEST AND IT IS NECESSARY DO NOT ALLOW A PERSON THAT HAS NOT ACCOUNT TO THIS PAGE.")
username = input("username: ")
password = input("password: ")
test_login(username, password)
number = int(input("Choose test type: 2-add car 3-delete car 4-confirm car 5-about button 6-question session: "))
if number == 2:
    image = "/media/esmaeil/A-data/FUM/software test/GHW1/crawler/audir8.png"
    test_add_car("audir8", "tabriz", "black", "50000", image, "iran", "0", "oil")
elif number == 3:
    test_delete_car()
elif number == 4:
    test_shopping_cart()
elif number == 5:
    test_about_button()
elif number == 6:
    test_question_session()


time.sleep(5)

driver.quit()