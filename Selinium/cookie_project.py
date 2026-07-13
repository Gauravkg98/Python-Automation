from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from selenium.common.exceptions import NoSuchElementException 

edge_Options = webdriver.EdgeOptions()
edge_Options.add_experimental_option("detach",True)

driver = webdriver.Edge(edge_Options)

driver.get("https://ohz.github.io/cookieclicker")

sleep(3)

print("Looking for Language selection")

try:
  language_button = driver.find_element(By.ID, value = "langSelect-EN")
  print("Found Language Button.........")
  language_button.click()
  sleep(3)
except NoSuchElementException:
  print(" Language Selection not found")

sleep(2)

#Find the cookie to click
cookie = driver.find_element(by=By.ID, value = "bigCookie")

item_ids = [f"product{i}" for i in range(18)]

wait_time = 5
timeout = time()+wait_time

five_min = time() +60*5

while True:

  cookie.click()
  if time()>timeout:
    try:
      cookies_element = driver.find_element(by=By.ID, value = "cookies")
      cookie_text = cookies_element.text
      cookie_count =int(cookie_text.split()[0].replace(",",""))

      products = driver.find_elements(by=By.CSS_SELECTOR, value ="div[id].........")

      best_item =None
      for product in reversed(products):
        if "enabled" in product.get_attribute("class"):
          best_item = product
          break

      if best_item:
        best_item.click()
        print(f"Bought item: {best_item.get_attribute('id')}")

    except (NoSuchElementException, ValueError):
      print("Couldn't find the cookie count or items")

    timeout = time+wait_time

  if time()>five_min:
    try:
      cookies_element = driver.find_element(by=By.ID, value ="cookies")
      print(f"Final Result : {cookies_element.text}")
    except NoSuchElementException:
      print("Couldn't get final cookie count")
    break



