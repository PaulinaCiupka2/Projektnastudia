#Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from time import sleep

#zmienne do formularzy
nazwisko = "Ciupka"
mail = "xyz@gmail.com"
haslo = "Testowanie123!"

#Stworzenie klasy do testow jednostkowych
class Rejestracja(unittest.TestCase):

#setUp konieczna Funkcja w tescie jednostkowym ustawiajaca poczatkowe warunki
    def setUp(self):
        #sterownik do przegladarki ustawia sie jako Chrome a nastepnie okno jest maksymalizowane
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

#BFnkcja z testem jednostkowym
    def test_wypelnienieFormularza(self):
        driver = self.driver #sterownik przypisany do zmiennej driver
        driver.get("https://www.eobuwie.com.pl/")  #sterownik otwiera strone
        driver.find_element(By.CLASS_NAME, "e-button--type-primary.e-button--color-brand.e-consents-alert__button.e-button").click() #sterownik zamyka cookies
        sleep(5) #program czeka 5 sekund
        driver.find_element(By.LINK_TEXT, 'Zarejestruj').click() #sterownik klika "Zarejestruj"
        # Wpisywanie wartości do formularza z wczesniej stworzonymi zmiennymi
        driver.find_element(By.ID, "lastname").send_keys(nazwisko)
        driver.find_element(By.ID, "email_address").send_keys(mail)
        driver.find_element(By.ID, "password").send_keys(haslo)
        driver.find_element(By.ID, "confirmation").send_keys(haslo)
        #Porgram klika "Oświadczam..." oraz przycik Rejestracja
        driver.find_element(By.XPATH, '//label[@class="checkbox-wrapper__label"]').click()
        driver.find_element(By.XPATH, '//button[@data-testid="register-create-account-button"]').click()
        #Zaznaczenie pola imie
        formularzImie = driver.find_element(By.NAME, "firstname")
        #Zdobycie wartości komunikatu o błędzie "To pole jest wymagane"
        error_span = driver.find_element(locate_with(By.XPATH, '//span[@class="form-error"]').near(formularzImie))
        #Test porownuje tekst wpisany jako pierwszy argument, ze zmienną zawierającą błąd ze strony
        self.assertEqual(u"To pole jest wymagane", error_span.text)

#Funkcja zamykajaca test jednostkowy
    def tearDown(self):
        self.driver.quit()


#Ten segment odpala test jednostkowy w konsoli
    if __name__ == "__main__":
        unittest.main()
