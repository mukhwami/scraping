"""
This module is used to srape data science job information on Brighter monday.
"""
import pandas as pd
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\Bob\Documents\scrape\web-scraping-job-postings\chromedriver_win32\chromedriver")

# Create empty DataFrame to store the data.
columns = [
    'title',
    'query',
    'company',
    'location',
    'emplo_type',
    'posted_date',
    'desc',
    'exp',
    'responsibilty',
    'education',
    'skills'
]
jobs = pd.DataFrame(columns=columns)

# Loop through 100 pages.
count = -1
category = ['data+scientist','data+analyst','machine+learning','business+analyst']
for query in category:
    for page in range(1):
        driver.get('https://www.jobspoint.co.ke/jobs/page/{}/?query={}&category'.format(page, query))
        for i in range(10):
                try:
                # Extract job title and location.
                    title_elem = "//div[@class='wpjb-page-index']/table/tbody/tr[{}]/td[2]/a".format(i+1)
                    comp_elem = "//div[@class='wpjb-page-index']/table/tbody/tr[{}]/td[2]/small".format(i+1)
                    emp_type_elem = "//div[@class='wpjb-page-index']/table/tbody/tr[{}]/td[3]/small".format(i+1)
                    posted_elem = "//div[@class='wpjb-page-index']/table/tbody/tr[{}]/td[4]".format(i+1)


                    title = driver.find_element_by_xpath(title_elem).text
                    company = driver.find_element_by_xpath(comp_elem).text
                    emplo_type = driver.find_element_by_xpath(emp_type_elem).text
                    posted_date = driver.find_element_by_xpath(posted_elem).text

                     # Click in job details.
                    card = driver.find_element_by_xpath("//div[@class='wpjb-page-index']/table/tbody/tr[{}]/td[2]/a".format(i+1))
                    try:
                        card.click()

                    except:

                        bar = driver.find_element_by_xpath("//div[@class='wpjb-page-index']/table/tbody/tr[{}]")
                        bar.click()
                        sleep(2)
                        card.click()

                    sleep(2)
                    try:
    #                     desc = driver.find_element_by_id('job-meta-company').text
                        desc = "//div[@class='wpjb-job-content']/div[1]"
                        exp = "//div[@class='site-content']/div[1]"
                        respons = "//div[@class='site-content']/div[2]"
                        edu = "//div[@class='site-content']/div[3]"
                        ski = "//div[@class='site-content']/div[4]"
                        loc_elem = "//div[@class='wpjb-job wpjb-page-single wpjb']/div/table/tbody/tr[2]/td[2]/span/span".format(i+1)
    #                     currency = "//div[@class='wpjb-main']/div/table/tbody/tr[6]/td[2]"


                        desc = driver.find_element_by_xpath(desc).text
                        exp = driver.find_element_by_xpath(exp).text
                        responsibilty = driver.find_element_by_xpath(respons).text
                        education = driver.find_element_by_xpath(edu).text
                        skills = driver.find_element_by_xpath(ski).text
                        location = driver.find_element_by_xpath(loc_elem).text
    #                     currency = driver.find_element_by_xpath(currency).text
                    except:
                        desc = None
                        expi = None
                        responsibilty = None
                        education = None
                        skills = None
                        currency = None
                        location = None


                    count += 1

                    # Save data in DataFrame.
                    jobs.loc[count] = [title, query, company, location, emplo_type, posted_date, desc, exp, responsibilty, education, skills]

                    driver.back()
                    sleep(3)

                # Terminate the loop at the last page.
                except:
                    break
jobs.to_csv('test.csv', index=False)
driver.close()
                  