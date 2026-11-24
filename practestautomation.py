import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPractice:
    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://practicetestautomation.com")
        driver.implicitly_wait(5)
        yield driver
        driver.quit()
        print("\nSuccessfully Executed.")

    def test_nav_prac(self, driver):
        practice_link = driver.find_element(By.XPATH, '//*[@id="menu-item-20"]/a')
        practice_link.click()

        assert driver.title == 'Practice | Practice Test Automation'
        driver.save_screenshot("test_nav_prac.png")

    def test_positive_login(self, driver):
        driver.find_element(By.XPATH, '//*[@id="menu-item-20"]/a').click()
        driver.find_element(By.LINK_TEXT, 'Test Login Page').click()

        driver.find_element(By.ID, "username").send_keys("student")
        time.sleep(0.5)
        driver.find_element(By.ID, "password").send_keys("Password123")
        time.sleep(0.5)
        driver.find_element(By.ID, "submit").click()
        time.sleep(0.5)

        assert "logged-in-successfully" in driver.current_url
        page_text =driver.find_element(By.TAG_NAME, "body").text
        assert "Congratulations" in page_text or "successfully logged in" in page_text

        logout = driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a')
        assert logout.is_displayed()
        driver.save_screenshot("test_click_login.png")

        logout.click()
        time.sleep(0.5)

    def test_negative_username(self, driver):
        driver.find_element(By.XPATH, '//*[@id="menu-item-20"]/a').click()
        driver.find_element(By.LINK_TEXT, 'Test Login Page').click()
        driver.find_element(By.ID, "username").send_keys("incorrectUser")
        time.sleep(0.5)
        driver.find_element(By.ID, "password").send_keys("Password123")
        time.sleep(0.5)
        driver.find_element(By.ID, "submit").click()
        time.sleep(0.5)

        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed()
        assert error_message.text == "Your username is invalid!"
        driver.save_screenshot("test_negative_username.png")

    def test_negative_password(self, driver):
        driver.find_element(By.XPATH, '//*[@id="menu-item-20"]/a').click()
        driver.find_element(By.LINK_TEXT, 'Test Login Page').click()

        driver.find_element(By.ID, "username").send_keys("student")
        time.sleep(0.5)
        driver.find_element(By.ID, "password").send_keys("incorrectPassword")
        time.sleep(0.5)
        driver.find_element(By.ID, "submit").click()
        time.sleep(0.5)

        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed()
        assert error_message.text == "Your password is invalid!"
        driver.save_screenshot("test_negative_password.png")


