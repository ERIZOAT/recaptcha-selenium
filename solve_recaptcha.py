
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def main():
    extension_path = os.path.abspath('./CapSolver.Browser.Extension')
    chrome_options = Options()
    chrome_options.add_argument(f'--load-extension={extension_path}')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.google.com/recaptcha/api2/demo')

    # Wait for the captcha to be solved automatically by the extension
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'recaptcha-demo-submit')))

    # Proceed with form submission or any other actions post-captcha solving
    driver.quit()

if __name__ == "__main__":
    main()
