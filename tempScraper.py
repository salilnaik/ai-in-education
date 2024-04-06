from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Selenium webdriver
driver = webdriver.Chrome()

# Navigate to the major maps page
driver.get("https://degrees.apps.asu.edu/majormaps")

# Find all the major map divs
major_map_divs = driver.find_elements(By.CSS_SELECTOR, "div.collegeAlphaName > span.majorDescriptionLink")

# Find the "Ira A. Fulton Schools of Engineering" major maps
engineering_major_maps = [div for div in major_map_divs if "Ira A. Fulton Schools of Engineering" in div.text]

# Click each "Ira A. Fulton Schools of Engineering" major map link and scrape the information
for major_map in engineering_major_maps:
    # Click the major map link
    major_map.click()
    
    # Find all the major map links under the "Required courses (Major Map)" section
    major_map_links = driver.find_elements(By.CSS_SELECTOR, "div.majorName > a")

    # Click each major map link and scrape the information
    for map_link in major_map_links:
        # Navigate to the major map page
        map_link.click()

        # Expand all the dropdowns
        dropdowns = driver.find_elements(By.CSS_SELECTOR, "i.chevron-icon.fa-chevron-down")
        for dropdown in dropdowns:
            dropdown.click()

        # Scrape the information from the dropdowns
        major_map_info = driver.find_elements(By.CSS_SELECTOR, "div.majorMapDesc")
        for info in major_map_info:
            print(info.text)

        # Go back to the previous page
        driver.back()

    # Go back to the major maps page
    driver.get("https://degrees.apps.asu.edu/majormaps")

# Close the webdriver
driver.quit()