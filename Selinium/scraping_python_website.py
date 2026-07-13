from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep edge browser open after program finish
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach",True)

driver = webdriver.Edge(edge_options)
driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
event ={}

for n in event_names:
  print(n.text)


for n in range(len(event_times)):

  event[n]={
    "time":event_times[n].text,
    "name":event_names[n].text
  }

print(event)
driver.close()
driver.quit()