import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'))
        )
        self.password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'))
        )
        self.login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'))
        )

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

def test_add_employee(driver):
    try:
        # Klik button PIM
        pim_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))
        )
        pim_button.click()

        # Klik Add Button
        add_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
        )
        add_button.click()

        # Isi form
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'))
        )
        middle_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'))
        )
        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'))
        )
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'))
        )

        first_name_input.send_keys("Rizki")
        middle_name_input.send_keys("Nur")
        last_name_input.send_keys("Asyifa")
        save_button.click()

        print("Employee added successfully.")
    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
    except TimeoutException as e:
        print(f"Error: Timeout occurred - {e}")
    except WebDriverException as e:
        print(f"Error: WebDriver exception occurred - {e}")

def test_login_and_add_employee():
    print("Starting Authentication and PIM test...")
    edge_options = Options()
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Page loaded.")

        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")

        dashboard_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.oxd-userdropdown-tab"))
        )

        print("Login successful, dashboard is present.")
        assert dashboard_element.is_displayed()

        test_add_employee(driver)  # Menambahkan test case PIM

        # Tunggu 60 detik sebelum keluar
        time.sleep(60)
        print("Waiting for 60 seconds...")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
    except TimeoutException as e:
        print(f"Error: Timeout occurred - {e}")
    except WebDriverException as e:
        print(f"Error: WebDriver exception occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_login_and_add_employee()
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'))
        )
        self.password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'))
        )
        self.login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'))
        )

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

def test_add_employee(driver):
    try:
        # Klik button PIM
        pim_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))
        )
        pim_button.click()

        # Klik Add Button
        add_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
        )
        add_button.click()

        # Isi form
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'))
        )
        middle_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'))
        )
        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'))
        )
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'))
        )

        first_name_input.send_keys("Rizki")
        middle_name_input.send_keys("Nur")
        last_name_input.send_keys("Asyifa")
        save_button.click()

        print("Employee added successfully.")
    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
    except TimeoutException as e:
        print(f"Error: Timeout occurred - {e}")
    except WebDriverException as e:
        print(f"Error: WebDriver exception occurred - {e}")

def test_login_and_add_employee():
    print("Starting Authentication and PIM test...")
    edge_options = Options()
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Page loaded.")

        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")

        dashboard_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.oxd-userdropdown-tab"))
        )

        print("Login successful, dashboard is present.")
        assert dashboard_element.is_displayed()

        test_add_employee(driver)  # Menambahkan test case PIM

        # Tunggu 60 detik sebelum keluar
        time.sleep(60)
        print("Waiting for 60 seconds...")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
    except TimeoutException as e:
        print(f"Error: Timeout occurred - {e}")
    except WebDriverException as e:
        print(f"Error: WebDriver exception occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_login_and_add_employee()
