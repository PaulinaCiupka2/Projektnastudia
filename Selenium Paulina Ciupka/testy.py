import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from time import sleep

# zmienne
nazwisko = "Ciupka"
mail = "xyz@gmail.com"
haslo = "Testowanie123!"


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.eobuwie.com.pl/")
driver.find_element(By.CLASS_NAME, "e-button--type-primary.e-button--color-brand.e-consents-alert__button.e-button").click()
sleep(5)
driver.find_element(By.LINK_TEXT, 'Zarejestruj').click()
# Wpisywanie wartości
driver.find_element(By.ID, "lastname").send_keys(nazwisko)
driver.find_element(By.ID, "email_address").send_keys(mail)
driver.find_element(By.ID, "password").send_keys(haslo)
driver.find_element(By.ID, "confirmation").send_keys(haslo)
driver.find_element(By.XPATH, '//label[@class="checkbox-wrapper__label"]').click()
driver.find_element(By.XPATH, '//button[@data-testid="register-create-account-button"]').click()
# Sprawdzenie bledu
formularzImie = driver.find_element(By.NAME, "firstname")
error_span = driver.find_element(locate_with(By.XPATH, '//span[@class="form-error"]').near(formularzImie))
# error_span2 = driver.find_element(locate_with(By.XPATH, '//span[@class="form-error"]').above(formularzNazwisko))
