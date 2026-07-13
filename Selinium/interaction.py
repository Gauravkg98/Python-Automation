from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach",True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

artice_count = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")

print(artice_count.text)

#find element by link text(hyperlink - the texts which are clickable)
all_porals = driver.find_element(By.LINK_TEXT, value="Content portals")

all_porals.click()


#Find the search <input> by Name
search = driver.find_element(By.NAME, "search")
#search = driver.find_element(By.LINK_TEXT,value='https://en.wikipedia.org/wiki/Special:Search')
search.click()

#Sending keyboard input to selenium
search.send_keys("Python",Keys.ENTER)


driver.close()
driver.quit()