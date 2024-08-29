# Solving reCaptcha Using Selenium and CapSolver Extension

This guide walks you through the process of setting up Selenium with the [CapSolver extension](https://www.capsolver.com/?utm_source=github&utm_medium=repo&utm_campaign=recaptchaextension) to solve reCaptcha v2. The method described can also be adapted to handle other types of CAPTCHAs.

## Table of Contents

- [1. Installing Selenium and Required Components](#1-installing-selenium-and-required-components)
- [2. Configuring the CapSolver Extension](#2-configuring-the-capsolver-extension)
- [3. Setting Up Selenium to Solve reCaptcha with CapSolver Extension](#3-setting-up-selenium-to-solve-recaptcha-with-capsolver-extension)
- [4. Full Code Example](#4-full-code-example)

## 1. Installing Selenium and Required Components

First, install Selenium and the necessary components using pip:

```bash
pip install selenium
```

Make sure to download and set up the appropriate drivers for the browser you plan to use (e.g., [ChromeDriver](https://sites.google.com/chromium.org/driver/) for Google Chrome, [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox).

## 2. Configuring the CapSolver Extension

Download the [CapSolver extension](https://github.com/capsolver/capsolver-browser-extension/releases/) and unzip it into a directory named `./CapSolver.Browser.Extension` at the root of your project.

### Configuration Settings

The extension provides various settings, including automatic CAPTCHA solving and proxy support. These are defined in the `./assets/config.json` file. Below is an example configuration:

```json
{
  "apiKey": "YourApiKey",
  "useCapsolver": true,
  "useProxy": false,
  "proxyType": "http",
  "hostOrIp": "",
  "port": "",
  "proxyLogin": "",
  "proxyPassword": "",
  "enabledForBlacklistControl": false,
  "blackUrlList": [],
  "enabledForRecaptcha": true,
  "enabledForRecaptchaV3": true,
  "enabledForHCaptcha": true,
  "enabledForFunCaptcha": true,
  "reCaptchaMode": "token",
  "hCaptchaMode": "click",
  "reCaptchaDelayTime": 0,
  "hCaptchaDelayTime": 0,
  "reCaptchaRepeatTimes": 10,
  "reCaptcha3RepeatTimes": 10,
  "hCaptchaRepeatTimes": 10,
  "funCaptchaRepeatTimes": 10
}
```

- **API Key**: Insert your CapSolver API key in the `apiKey` field. You can obtain your API key from the [CapSolver Dashboard](https://www.capsolver.com/?utm_source=github&utm_medium=repo&utm_campaign=recaptchaextension).
- **Modes**: For this example, `reCaptchaMode` is set to `token`, but you can also use the `click` mode for reCaptcha.

For detailed documentation on CapSolver's features, visit the [CapSolver Documentation](https://docs.capsolver.com/en/guide/getting-started/?utm_source=github&utm_medium=repo&utm_campaign=recaptchaextension).

## 3. Setting Up Selenium to Solve reCaptcha with CapSolver Extension

Now, let's set up Selenium WebDriver and configure it to use the CapSolver extension. Below is an example using ChromeDriver in Python:

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
```

## 4. Full Code Example

The Python script provided above is ready to run. Ensure your environment is correctly set up with the necessary packages and drivers, and adjust the `extension_path` if needed to point to your CapSolver extension directory.

By following these steps, you've successfully configured Selenium with the CapSolver Extension to solve reCaptcha v2 using Python. This method can be easily adapted to solve other types of CAPTCHAs by making minor adjustments.

For more information on CapSolver, check out the [CapSolver Documentation](https://docs.capsolver.com/en/guide/getting-started/?utm_source=github&utm_medium=repo&utm_campaign=recaptchaextension) or visit the [CapSolver Website](https://www.capsolver.com/?utm_source=github&utm_medium=repo&utm_campaign=recaptchaextension).


<img width="960" alt="CapSolver" src="https://github.com/user-attachments/assets/fd9449e8-a6c4-4ec3-8bd7-8d6e107f1134">

