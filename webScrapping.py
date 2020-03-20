#Importing the necessary libraries
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd 

path = "C:\\Users\123\Desktop\webScrap"

url="Put the web Address here"

#Please note that some system work on without providing path to Chrome function
driver = webdriver.Chrome()
driver.get(url)
elem = driver.find_element_by_link_text("Online Fire Report")

elem.get_attribute('href')
#Returs link

elem.click()

elem = driver.find_element_by_link_text("On-Line Fire Report")
elem.click()

#Bypassing Alert/Popup
driver.switch_to_alert().accept()

elem = driver.find_element_by_link_text("View Fire Report")
elem.click()

#Bypassing radio button

elem = driver.find_elements_by_id("Radio5")
elem.click()

"""
# click radio button
python_button = driver.find_elements_by_xpath("//input[@name='save' and @value='View Fire Report']")[0]
python_button.click()

"""
"""
#Filling the form

# type text
text_area = driver.find_element_by_id('textarea')
text_area.send_keys("print('Hello World')")

# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
submit_button.click()

"""

#Scrapping the main data

Fire_Report_Number=[] 
Operational_Jurisdiction_of_Fire_Station=[] 
Information_Received_From=[] 

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'reg'}):
name=a.find('td', attrs={'class':'txt'})
price=a.find('td', attrs={'class':'txt'})
rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text)



#Storing the data in csv format
df = pd.DataFrame({'Station  Name':Std_name,Rating':ratings}) 
df.to_csv('FireStation.csv', index=False, encoding='utf-8')
