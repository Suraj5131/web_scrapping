from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

chromedriver_path = "C:/Program Files (x86)/Google/Chrome/Application/"
chrome_options.add_argument("webdriver.chrome.driver=" + chromedriver_path)

driver = webdriver.Chrome(options=chrome_options)
url = 'https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx'
driver.get(url)
time.sleep(2)
driver.refresh()

start_date_input_xpath = "//input[@name='ctl00$ContentPlaceHolder1$txtDateOfRegistrationFrom']"
end_date_input_xpath = "//input[@name='ctl00$ContentPlaceHolder1$txtDateOfRegistrationTo']"
district_dropdown_xpath = "//select[@name='ctl00$ContentPlaceHolder1$ddlDistrict']"
search_button_xpath = "//input[@name='ctl00$ContentPlaceHolder1$btnSearch']"
page_size_dropdown_xpath = "//select[@name='ctl00$ContentPlaceHolder1$ucRecordView$ddlPageSize']"

from_date_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, start_date_input_xpath)))

from_date_input.clear()
from_date_input.send_keys("23/3/5")

to_date_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, end_date_input_xpath)))

to_date_input.clear()
to_date_input.send_keys("2023/3/6")

district_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, district_dropdown_xpath)))

district_select = Select(district_dropdown)
district_select.select_by_visible_text("PUNE CITY")

search_button = driver.find_element(By.XPATH, search_button_xpath)

search_button.click()

page_size_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, page_size_dropdown_xpath)))

page_size_select = Select(page_size_dropdown)
page_size_select.select_by_value("50")
driver.refresh()
time.sleep(5)

table_xpath = "//table[@id='ContentPlaceHolder1_gdvDeadBody']"
table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))

rows = table.find_elements(By.TAG_NAME, "tr")[1:51]  # Skip the header row and limit to the first 50 rows

data = []
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = {
        "Sr.NO.":cells[0].text,
        "State":cells[1].text,
        "District":cells[2].text,
        "Police Station": cells[3].text,
        "Year":cells[4].text,
        "FIR Number": cells[5].text,
        "Date of Registration": cells[6].text,
        "Sections":cells[8].text,
    }
    data.append(row_data)

csv_file_path = "FIR_DATA_.csv"

with open(csv_file_path, "w", newline="", encoding="utf-16") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
print("Data extraction complete.")

second_page_link_xpath = "//a[@href=\"javascript:__doPostBack('ctl00$ContentPlaceHolder1$gdvDeadBody','Page$2')\"]"
second_page_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, second_page_link_xpath)))

driver.execute_script("arguments[0].click();", second_page_link)
print("Load second Page")
time.sleep(15)

table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))

rows = table.find_elements(By.TAG_NAME, "tr")[1:101]

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = {
        "Sr.NO.": cells[0].text,
        "State": cells[1].text,
        "District": cells[2].text,
        "Police Station": cells[3].text,
        "Year": cells[4].text,
        "FIR Number": cells[5].text,
        "Date of Registration": cells[6].text,
        "Sections": cells[8].text,
    }
    data.append(row_data)

with open(csv_file_path, "a", newline="", encoding="utf-16") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writerows(data[len(data)-len(rows):])  # Write only the newly added rows

time.sleep(15)
print("Data 2 extraction complete.")

third_page_link_xpath = "//a[@href=\"javascript:__doPostBack('ctl00$ContentPlaceHolder1$gdvDeadBody','Page$3')\"]"
third_page_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, third_page_link_xpath)))

driver.execute_script("arguments[0].click();", third_page_link)
print("Load third Page")
time.sleep(15)

table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))

rows = table.find_elements(By.TAG_NAME, "tr")[1:151]

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = {
        "Sr.NO.": cells[0].text,
        "State": cells[1].text,
        "District": cells[2].text,
        "Police Station": cells[3].text,
        "Year": cells[4].text,
        "FIR Number": cells[5].text,
        "Date of Registration": cells[6].text,
        "Sections": cells[8].text,
    }
    data.append(row_data)

with open(csv_file_path, "a", newline="", encoding="utf-16") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writerows(data[len(data)-len(rows):])
print("Data 3 extraction complete.")

fourth_page_link_xpath = "//a[@href=\"javascript:__doPostBack('ctl00$ContentPlaceHolder1$gdvDeadBody','Page$4')\"]"
fourth_page_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, fourth_page_link_xpath)))

driver.execute_script("arguments[0].click();", fourth_page_link)
print("Load fourth Page")
time.sleep(15)

table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))

rows = table.find_elements(By.TAG_NAME, "tr")[1:201]

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = {
        "Sr.NO.": cells[0].text,
        "State": cells[1].text,
        "District": cells[2].text,
        "Police Station": cells[3].text,
        "Year": cells[4].text,
        "FIR Number": cells[5].text,
        "Date of Registration": cells[6].text,
        "Sections": cells[8].text,
    }
    data.append(row_data)

with open(csv_file_path, "a", newline="", encoding="utf-16") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writerows(data[len(data)-len(rows):])  # Write only the newly added rows

time.sleep(15)
print("Data 4 extraction complete.")

fifth_page_link_xpath = "//a[@href=\"javascript:__doPostBack('ctl00$ContentPlaceHolder1$gdvDeadBody','Page$5')\"]"
fifth_page_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, fifth_page_link_xpath)))

driver.execute_script("arguments[0].click();", fifth_page_link)
print("Load fifth Page")
time.sleep(15)

table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))

rows = table.find_elements(By.TAG_NAME, "tr")[1:251]

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = {
        "Sr.NO.": cells[0].text,
        "State": cells[1].text,
        "District": cells[2].text,
        "Police Station": cells[3].text,
        "Year": cells[4].text,
        "FIR Number": cells[5].text,
        "Date of Registration": cells[6].text,
        "Sections": cells[8].text,
    }
    data.append(row_data)

with open(csv_file_path, "a", newline="", encoding="utf-16") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writerows(data[len(data)-len(rows):])  # Write only the newly added rows

time.sleep(15)
print("Data 5 extraction complete.")

sixth_page_link_xpath = "//a[@href=\"javascript:__doPostBack('ctl00$ContentPlaceHolder1$gdvDeadBody','Page$6')\"]"
sixth_page_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, sixth_page_link_xpath)))

driver.execute_script("arguments[0].click();", sixth_page_link)
print("Load sixth Page")
time.sleep(15)

table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))

rows = table.find_elements(By.TAG_NAME, "tr")[1:301]

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = {
        "Sr.NO.": cells[0].text,
        "State": cells[1].text,
        "District": cells[2].text,
        "Police Station": cells[3].text,
        "Year": cells[4].text,
        "FIR Number": cells[5].text,
        "Date of Registration": cells[6].text,
        "Sections": cells[8].text,
    }
    data.append(row_data)

with open(csv_file_path, "a", newline="", encoding="utf-16") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writerows(data[len(data)-len(rows):])  # Write only the newly added rows

time.sleep(15)
print("Data 6 extraction complete.")

seventh_page_link_xpath = "//a[@href=\"javascript:__doPostBack('ctl00$ContentPlaceHolder1$gdvDeadBody','Page$7')\"]"
seventh_page_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, seventh_page_link_xpath)))

driver.execute_script("arguments[0].click();", seventh_page_link)
print("Load seventh Page")
time.sleep(15)

table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))

rows = table.find_elements(By.TAG_NAME, "tr")[1:351]

eighth_page_link_xpath = "//a[@href=\"javascript:__doPostBack('ctl00$ContentPlaceHolder1$gdvDeadBody','Page$8')\"]"
eighth_page_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, eighth_page_link_xpath)))

driver.execute_script("arguments[0].click();", eighth_page_link)
print("Load eighth Page")
time.sleep(15)

table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))

rows = table.find_elements(By.TAG_NAME, "tr")[1:]

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = {
        "Sr.NO.": cells[0].text,
        "State": cells[1].text,
        "District": cells[2].text,
        "Police Station": cells[3].text,
        "Year": cells[4].text,
        "FIR Number": cells[5].text,
        "Date of Registration": cells[6].text,
        "Sections": cells[8].text,
    }
    data.append(row_data)

with open(csv_file_path, "a", newline="", encoding="utf-16") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writerows(data[len(data)-len(rows):])

time.sleep(15)
print("Data 8 extraction complete.")

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = {
        "Sr.NO.": cells[0].text,
        "State": cells[1].text,
        "District": cells[2].text,
        "Police Station": cells[3].text,
        "Year": cells[4].text,
        "FIR Number": cells[5].text,
        "Date of Registration": cells[6].text,
        "Sections": cells[8].text,
    }
    data.append(row_data)

with open(csv_file_path, "a", newline="", encoding="utf-16") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writerows(data[len(data)-len(rows):])  # Write only the newly added rows

time.sleep(15)
print("Data 7 extraction complete.")

driver.quit()

print("Data extraction complete.")
print(f"The first 50 records have been saved in '{csv_file_path}' (CSV) file.")