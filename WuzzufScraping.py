# ===================================================
# Program : Wuzzuf Scraping
# Author  : Alhasan Gamal Mahmoud
# Version : V1.0
# Date    : 02-01-2022
# =====================================================

# # * import libaries
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# import time
# import dateutil.relativedelta
# import datetime
# import csv
# import random
# import threading as th
# import psycopg2

# # * Establishing the connection
# conn = psycopg2.connect(
#     database="Wuzzuf", user='postgres', password='123456', host='127.0.0.1', port='5432'
# )
# # * Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# # * Setting auto commit false
# conn.autocommit = True

# # * Chrome deriver path
# chrome_path = r"C:\Users\Alhasan Gamal\Desktop\ITI-AI Pro\Data Prepration\chromedriver_win32\chromedriver.exe"

# # * Opening chrom driver session
# option = webdriver.ChromeOptions()
# option.add_argument("disk-cache-size=3000000000")
# driver = webdriver.Chrome(chrome_path)

# # * to get Website
# driver.get('https://wuzzuf.net/jobs/egypt')
# driver.maximize_window()

# # * pase value to searchplace and search it
# searchplace = driver.find_element_by_css_selector('input.search-bar-input')
# searchplace.send_keys("python")
# searchplace.send_keys(Keys.ENTER)

# # * Get data from website
# title = driver.find_elements_by_css_selector(' h2 > a')
# company = driver.find_elements_by_css_selector(
#     'div > div.css-laomuu > div > a')
# address = driver.find_elements_by_css_selector(
#     'div > div.css-laomuu > div > span')
# date = driver.find_elements_by_css_selector('div > div.css-laomuu > div > div')
# type = driver.find_elements_by_css_selector('div.css-1lh32fc > a > span')
# experience = driver.find_elements_by_css_selector(
#     'div > div.css-y4udm8 > div:nth-child(2) > span')

# for i in range(len(title)):
#     j_title = title[i].text
#     j_company = company[i].text[:-2]
#     j_address = address[i].text
#     if int(date[i].text[0]) < 9:
#         if date[i].text[2:-4] == "days":
#             j_time = datetime.datetime.now(
#             ) - datetime.timedelta(int(date[i].text[0]))
#         elif date[i].text[2:-4] == "hours":
#             j_time = datetime.datetime.now(
#             ) - datetime.timedelta(hours=int(date[i].text[0]))
#         else:
#             j_time = datetime.datetime.now(
#             ) - dateutil.relativedelta.relativedelta(months=int(date[i].text[0]))
#     else:
#         if date[i].text[2:-4] == "days":
#             j_time = datetime.datetime.now(
#             ) - datetime.timedelta(int(date[i].text[0]))

#         elif date[i].text[2:-4] == "hours":
#             j_time = datetime.datetime.now(
#             ) - datetime.timedelta(hours=int(date[i].text[0]))

#         else:
#             j_time = datetime.datetime.now(
#             ) - dateutil.relativedelta.relativedelta(months=int(date[i].text[0]))
#     j_type = type[i].text
#     j_exp = experience[i].text[2:]

#     sql = '''INSERT INTO public."Job"("Title","Company","Address","Date","Type","Experience") VALUES (%s,%s,%s,%s,%s,%s)'''
#     data = (j_title, j_company, j_address, str(j_time)[0:10], j_type, j_exp)
#     cursor.execute(sql, data)
#     conn.commit()

# print("Records inserted")

# conn.close()
# driver.close()
# ============================================================================

# ===================================================
# Program : Wuzzuf Scraping
# Author  : Alhasan Gamal Mahmoud
# Version : V1.1
# Date    : 03-01-2022
# =====================================================

# * import libaries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import dateutil.relativedelta
import datetime
import csv
import random
import threading as th
import psycopg2

# * Establishing the connection
conn = psycopg2.connect(
    database="Wuzzuf", user='postgres', password='123456', host='127.0.0.1', port='5432'
)
# * Creating a cursor object using the cursor() method
cursor = conn.cursor()

# * Setting auto commit false
conn.autocommit = True

# * Chrome deriver path
chrome_path = r"C:\Users\Alhasan Gamal\Desktop\ITI-AI Pro\Data Prepration\chromedriver_win32\chromedriver.exe"

# * Opening chrom driver session
option = webdriver.ChromeOptions()
option.add_argument("disk-cache-size=3000000000")
driver = webdriver.Chrome(chrome_path)

# * to get Website
driver.get('https://wuzzuf.net/jobs/egypt')
driver.maximize_window()

# * make a list of search keys
my_list = ["python", "machine learning"]

# * pase value to searchplace and search it
searchplace = driver.find_element_by_css_selector('input.search-bar-input')
searchplace.send_keys(my_list[0])
searchplace.send_keys(Keys.ENTER)
time.sleep(2)
# * get number of job in each page
job_per_page = driver.find_elements_by_css_selector(
    'div[class="css-1gatmva e1v1l3u10"]')

# * get number of page
num_jobs = driver.find_element_by_tag_name('strong')
num_pages = round(int(num_jobs.text) / len(job_per_page))


# * get job data about python from each page
for i in range(num_pages):
    exp = []
    driver.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={i}")
    time.sleep(2)

    title = driver.find_elements_by_css_selector(' h2 > a')
    company = driver.find_elements_by_css_selector(
        'div > div.css-laomuu > div > a')
    address = driver.find_elements_by_css_selector(
        'div > div.css-laomuu > div > span')
    date = driver.find_elements_by_css_selector(
        'div > div.css-laomuu > div > div')
    type = driver.find_elements_by_css_selector('div.css-1lh32fc > a > span')
    time.sleep(4)
    job_per_page = driver.find_elements_by_css_selector(
        'div[class="css-1gatmva e1v1l3u10"]')
    for job in job_per_page:
        try:
            experience = job.find_element_by_css_selector(
                'div > div.css-y4udm8 > div:nth-child(2) > span')
            exp.append(experience.text[2:])

        except:
            experience = job.find_element_by_css_selector(
                'div > div.css-y4udm8 > div:nth-child(2) > a')
            exp.append(experience.text)

    for j in range(len(title)):
        j_title = title[j].text
        j_company = company[j].text[:-2]
        j_address = address[j].text
        if int(date[j].text[0]) < 9:
            if date[j].text[2:-4] == "days":
                j_time = datetime.datetime.now(
                ) - datetime.timedelta(int(date[j].text[0]))
            elif date[j].text[2:-4] == "hours":
                j_time = datetime.datetime.now(
                ) - datetime.timedelta(hours=int(date[j].text[0]))
            else:
                j_time = datetime.datetime.now(
                ) - dateutil.relativedelta.relativedelta(months=int(date[j].text[0]))
        else:
            if date[j].text[2:-4] == "days":
                j_time = datetime.datetime.now(
                ) - datetime.timedelta(int(date[j].text[0]))

            elif date[j].text[2:-4] == "hours":
                j_time = datetime.datetime.now(
                ) - datetime.timedelta(hours=int(date[j].text[0]))

            else:
                j_time = datetime.datetime.now(
                ) - dateutil.relativedelta.relativedelta(months=int(date[j].text[0]))
        j_type = type[j].text
        j_exp = exp[j]

        sql = '''INSERT INTO public."Python_Job"("Title","Company","Address","Date","Type","Experience") VALUES (%s,%s,%s,%s,%s,%s)'''
        data = (j_title, j_company, j_address,
                str(j_time)[0:10], j_type, j_exp)
        cursor.execute(sql, data)
        conn.commit()


# * to get Website
driver.get('https://wuzzuf.net/jobs/egypt')


# * pase value to searchplace and search it
searchplace = driver.find_element_by_css_selector('input.search-bar-input')
searchplace.send_keys(my_list[1])
searchplace.send_keys(Keys.ENTER)
time.sleep(2)
# * get number of job in each page
job_per_page = driver.find_elements_by_css_selector(
    'div[class="css-1gatmva e1v1l3u10"]')

# * get number of page
num_jobs = driver.find_element_by_tag_name('strong')
num_pages = round(int(num_jobs.text) / len(job_per_page))

# * get job data about machine learning from each page
for i in range(num_pages):
    exp = []
    driver.get(
        f"https://wuzzuf.net/search/jobs/?a=spbg&q=machine%20learning&start={i}")
    time.sleep(2)
    title = driver.find_elements_by_css_selector(' h2 > a')
    company = driver.find_elements_by_css_selector(
        'div > div.css-laomuu > div > a')
    address = driver.find_elements_by_css_selector(
        'div > div.css-laomuu > div > span')
    date = driver.find_elements_by_css_selector(
        'div > div.css-laomuu > div > div')
    type = driver.find_elements_by_css_selector('div.css-1lh32fc > a > span')
    time.sleep(4)
    job_per_page = driver.find_elements_by_css_selector(
        'div[class="css-1gatmva e1v1l3u10"]')
    for job in job_per_page:
        try:
            experience = job.find_element_by_css_selector(
                'div > div.css-y4udm8 > div:nth-child(2) > span')
            exp.append(experience.text[2:])

        except:
            experience = job.find_element_by_css_selector(
                'div > div.css-y4udm8 > div:nth-child(2) > a')
            exp.append(experience.text)

    for j in range(len(title)):
        j_title = title[j].text
        j_company = company[j].text[:-2]
        j_address = address[j].text
        if int(date[j].text[0]) < 9:
            if date[j].text[2:-4] == "days":
                j_time = datetime.datetime.now(
                ) - datetime.timedelta(int(date[j].text[0]))
            elif date[j].text[2:-4] == "hours":
                j_time = datetime.datetime.now(
                ) - datetime.timedelta(hours=int(date[j].text[0]))
            else:
                j_time = datetime.datetime.now(
                ) - dateutil.relativedelta.relativedelta(months=int(date[j].text[0]))
        else:
            if date[j].text[2:-4] == "days":
                j_time = datetime.datetime.now(
                ) - datetime.timedelta(int(date[j].text[0]))

            elif date[j].text[2:-4] == "hours":
                j_time = datetime.datetime.now(
                ) - datetime.timedelta(hours=int(date[j].text[0]))

            else:
                j_time = datetime.datetime.now(
                ) - dateutil.relativedelta.relativedelta(months=int(date[j].text[0]))
        j_type = type[j].text
        j_exp = exp[j]

        sql = '''INSERT INTO public."Machine_Learning"("Title","Company","Address","Date","Type","Experience") VALUES (%s,%s,%s,%s,%s,%s)'''
        data = (j_title, j_company, j_address,
                str(j_time)[0:10], j_type, j_exp)
        cursor.execute(sql, data)
        conn.commit()


conn.close()
driver.close()
