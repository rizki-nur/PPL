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

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        try:
            # Klik dropdown user
            user_dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.oxd-userdropdown-tab"))
            )
            user_dropdown.click()

            # Klik link logout
            logout_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@role='menuitem' and text()='Logout']"))
            )
            logout_link.click()

            # Tunggu hingga kembali ke halaman login
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'))
            )
        except NoSuchElementException as e:
            print(f"Error: Element not found - {e}")
        except TimeoutException as e:
            print(f"Error: Timeout occurred - {e}")
        except WebDriverException as e:
            print(f"Error: WebDriver exception occurred - {e}")

def test_repeated_login_logout(times):
    print("Starting Authentication test...")
    edge_options = Options()
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

    try:
        for _ in range(times):
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            print(f"Attempt {_ + 1}: Page loaded.")

            login_page = LoginPage(driver)
            login_page.login("Admin", "admin123")

            dashboard_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.oxd-userdropdown-tab"))
            )

            print(f"Attempt {_ + 1}: Login successful, dashboard is present.")
            assert dashboard_element.is_displayed()

            dashboard_page = DashboardPage(driver)
            dashboard_page.logout()

            WebDriverWait(driver, 10).until(
                lambda driver: driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
            )

            print(f"Attempt {_ + 1}: Logout successful, returned to login page.")

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
    import sys
    if len(sys.argv) > 1:
        try:
            test_repeated_login_logout(int(sys.argv[1]))
        except ValueError:
            print("Please provide a valid number of times as an argument.")
    else:
        test_repeated_login_logout(100)
