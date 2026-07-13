from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
edge_Options = webdriver.EdgeOptions()
edge_Options.add_experimental_option("detach",True)

driver = webdriver.Edge(edge_Options)

driver.get("https://appbrewery.github.io/fake-newsletter-singup")

fname = driver.find_element(By.NAME,value="fName")
lname = driver.find_element(By.NAME,value="lName")
mail  = driver.find_element(By.NAME,value="email")

#Fill out form

fname.send_keys("gk789098")
lname.send_keys("67890-0987")
mail.send_keys("gakj@89098gmail.com")

#Locate the signup button. then click it

submit = driver.find_element(By.CSS_SELECTOR,value="form button")
submit.click()