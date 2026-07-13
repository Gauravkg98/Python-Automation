from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep Edge browser open after script finishes
edge_options = Options()
edge_options.add_experimental_option("detach", True)

# Start Edge WebDriver with options
driver = webdriver.Edge(options=edge_options)

driver.get("https://www.amazon.in/Havells-Hexo-Plus-Jar-IPolycarbonate/dp/B0CPYMQDGN")

try:
    # Wait until price elements load
    wait = WebDriverWait(driver, 15)

    price_rupees = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
    )

    price_paise = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-fraction"))
    )

    print("Current Price:", price_rupees.text + "." + price_paise.text)

except Exception as e:
    print("Error:", e)
