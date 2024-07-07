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

def test_buzz_post(driver):
    try:
        # Klik button Buzz
        buzz_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a'))
        )
        buzz_button.click()

        # Tunggu beberapa saat hingga halaman Buzz terbuka
        time.sleep(2)

        # Isi form postingan
        post_textarea = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea.oxd-buzz-post-input'))
        )
        post_textarea.click()  # Klik textarea untuk mengaktifkannya

        post_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.oxd-buzz-post-slot button[type="submit"]'))
        )

        # Mengisi dan memposting
        post_textarea.send_keys("Ini Testing...")
        time.sleep(1)  # Tunggu sejenak setelah mengisi teks
        post_button.click()

        print("Buzz post added successfully.")
    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
    except TimeoutException as e:
        print(f"Error: Timeout occurred - {e}")
    except WebDriverException as e:
        print(f"Error: WebDriver exception occurred - {e}")

def test_login_and_buzz_post():
    print("Starting Authentication and Buzz test...")
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

        test_buzz_post(driver)  # Menambahkan test case buzz post

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
    test_login_and_buzz_post()
