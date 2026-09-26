from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime

# =========================
# Settings
# =========================

url = "https://www.gomo.sg/plan-detail/98"

# Numbers to search for
search_strings = ["1747"]

# =========================
# Chrome options
# =========================

chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option(
    "excludeSwitches",
    ["enable-logging"]
)

# =========================
# Start Chrome
# =========================

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

count = 0

try:
    while True:

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ==========================================
        # Click "See more"
        # ==========================================

        try:
            show_more_button = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[.//span[normalize-space()='See more']]"
                    )
                )
            )

            show_more_button.click()

            print(f"'See more' clicked at {current_time}")

            # Allow additional numbers to load
            time.sleep(1)

        except TimeoutException:
            print(f"No 'See more' button found at {current_time}")

        # ==========================================
        # Find all phone numbers
        # ==========================================

        number_elements = driver.find_elements(
            By.CSS_SELECTOR,
            "span.number___Ctm64"
        )

        print(f"Found {len(number_elements)} numbers")

        # ==========================================
        # Search for target number
        # ==========================================

        found = False

        for element in number_elements:

            number_text = element.text.strip()

            print(f"Checking: {number_text}")

            # Remove the space so:
            # "8436 0512" becomes "84360512"
            clean_number = number_text.replace(" ", "")

            for search_string in search_strings:

                if clean_number.endswith(search_string):
                    print(
                        f"FOUND: '{number_text}' "
                        f"contains target ending '{search_string}' "
                        f"at {current_time}"
                    )

                    found = True
                    break

            if found:
                break

        # ==========================================
        # Target found
        # ==========================================

        if found:

            print("====================================")
            print("TARGET NUMBER FOUND!")
            print("Browser will remain open.")
            print("Press Ctrl+C to stop the script.")
            print("====================================")

            while True:
                time.sleep(10)

        # ==========================================
        # Target not found
        # ==========================================

        else:

            count += 1

            print(
                f"[{count}] Target number not found. "
                f"Refreshing page at {current_time}"
            )

            driver.refresh()

            # Wait for page to reload
            time.sleep(1)

# ==========================================
# Stop with Ctrl+C
# ==========================================

except KeyboardInterrupt:

    print("\nScript stopped by user.")

# ==========================================
# Other errors
# ==========================================

except Exception as e:

    print(f"An error occurred: {e}")

# ==========================================
# Always close browser
# ==========================================

finally:

    driver.quit()