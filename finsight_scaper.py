from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = "/Users/jhalverson/Downloads/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

def write_csv(labels, rows, title, idx):
    flnm = title.replace(" ", "").lower() + str(idx) +  ".csv"
    labels = [label.text for label in labels]
    num_cols = len(labels)
    num_rows = len(rows) // num_cols
    assert len(rows) % num_cols == 0
    with open(flnm, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(labels)
        for i in range(num_rows):
            row = [rows[j].text for j in range(i * num_cols, (i + 1) * num_cols)]
            writer.writerow(row)

for idx in range(47676, 47677 + 1):
    url = f"https://finsight.com/deal/{idx}"
    driver.get(url)

    #try:
    #    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app")))
    #except:
    #    driver.quit()
    sleep(5)
    #print(driver.page_source)
    labels = driver.find_elements_by_tag_name('th')
    rows = driver.find_elements_by_tag_name('td')
    write_csv(labels, rows, driver.title, idx)
driver.quit()
