from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#this code close the webiste instantly after opening it
#driver = webdriver.Edge()
#driver.get("https://www.amazon.com")

#Keep edge browser open after program finish
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach",True)

driver = webdriver.Edge(edge_options)
driver.get("https://www.amazon.in/Havells-Hexo-Plus-Jar-IPolycarbonate/dp/B0CPYMQDGN/ref=sr_1_2_sspa?crid=2U5USE7H87SQ2&dib=eyJ2IjoiMSJ9.v6evp1nL3qmtd_57kTo8dsDCpGWwB7GPMw_3XuWujaxU2z8kwAwOHJTTjfwij3hFZH22PF6lM3ki5qeQRn3Mi33ZMwce-gZfja_SooAGBhXcj5b6mvK82H0c1ytSRGlxssViXt1psmG0KOXrIV_sp_7zL5y2KydewS08UGB3wBcb5T3lORNlsmJJvzYk9mTgE2_LzvCEjGDWnD_3o6uklC_1kCPU80GTnX2CAFQVqEkGtjtcQw2x6DmqCCL8rOxNn_DRzSab5c2stmwMzrMJZevpN_6AFPjTGFG8ySRahY4.SFJFPUTZZQiLWMo5_WFZdqwDimOlivBBEw7MkewmtOM&dib_tag=se&keywords=havells%2Bmixer%2Bgrinder&qid=1779566070&sprefix=havelles%2Bmixer%2Bgrinder%2Caps%2C322&sr=8-2-spons&aref=CjcnpZJwfx&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
wait = WebDriverWait(driver, 15)

price_rupees = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))
price_paise = driver.find_element(By.CLASS_NAME, value = "a-price-whole")

print(f"The Current Price is {price_rupees.text}, {price_paise.text}")

search_bar = driver.find_element(By.NAME,value="q")
print(search_bar)
button = driver.find_element(By.ID, value ="submit")
print(button.size)

doc_link =driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(doc_link.text)



link_t=driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/ul/li[3]/a')
print(link_t.text)


#driver.close()
#driver.quit()
