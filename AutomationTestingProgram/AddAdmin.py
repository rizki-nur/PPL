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

def select_dropdown_option(driver, dropdown_xpath, option_text):
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
    )
    dropdown.click()
    option_xpath = f"//div[@role='listbox']//span[text()='{option_text}']"
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, option_xpath))
    )
    option.click()

def test_add_admin(driver):
    try:
        # Klik button Admin
        admin_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
        )
        admin_button.click()

        # Klik Add Button
        add_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
        )
        add_button.click()

        # Isi form
        user_role_select_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
        select_dropdown_option(driver, user_role_select_xpath, "Admin")

        employee_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input'))
        )
        status_select_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'
        select_dropdown_option(driver, status_select_xpath, "Enabled")

        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input'))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'))
        )
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'))
        )
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]'))
        )

        # Mengisi data pada form
        employee_name_input.send_keys("Rizki Nur Asyifa")
        username_input.send_keys("Rizki2002")
        password_input.send_keys("Riski-2002")
        confirm_password_input.send_keys("Riski-2002")
        save_button.click()

        print("Admin added successfully.")
    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
    except TimeoutException as e:
        print(f"Error: Timeout occurred - {e}")
    except WebDriverException as e:
        print(f"Error: WebDriver exception occurred - {e}")

def test_login_and_add_admin():
    print("Starting Authentication and Admin test...")
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

        test_add_admin(driver)  # Menambahkan test case admin

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
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_and_add_admin()
