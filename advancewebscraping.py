# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import csv
#
# # Set up Selenium WebDriver
# service = Service("C:\\Users\\BHARATH\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
#
# # Open Naukri's Python Jobs page
# driver.get(
#     "https://www.naukri.com/python-jobs?k=python&qproductJobSource=2&naukriCampus=true&experience=0&nignbevent_src=jobsearchDeskGNB")
#
# # Wait until the page is loaded and the job listings are available
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper")))
#
# # Extract job details
# jobs = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
# print(f"Total Jobs Found: {len(jobs)}")
#
# # Create and write to a CSV file
# csv_file = "job_listings.csv"
# with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Title", "Company", "Location", "Posted Date", "Job Link"])  # Added "Posted Date" & "Job Link"
#
#     for job in jobs:
#         try:
#             # Extract Job Title
#             title = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]").text.strip()
#
#             # Extract Company Name
#             company = job.find_element(By.XPATH, ".//a[contains(@class, 'comp-name')]").text.strip()
#
#             # Extract Job Location
#             location = job.find_element(By.XPATH, ".//span[contains(@class,'locWdth')]").text.strip()
#
#             # Extract Posted Date (Updated XPath)
#             #styles_jhc__stat__PgY67
#             try:
#                 posted_date_element = WebDriverWait(job, 5).until(
#                     EC.presence_of_element_located(
#                         (By.XPATH, ".//span[contains(@class, 'job-post-day')]/span"))
#                 )
#                 posted_date = posted_date_element.text.strip()
#             except:
#                 posted_date = "Unknown"  # If it fails, set "Unknown"
#
#             # Extract Job Link
#             job_link = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]").get_attribute("href")
#
#             # Print job details to console
#             print(f"Title: {title}")
#             print(f"Company: {company}")
#             print(f"Location: {location}")
#             print(f"Posted: {posted_date}")
#             print(f"Job Link: {job_link}")
#             print("-" * 50)
#
#             # Write job details to CSV file
#             writer.writerow([title, company, location, posted_date, job_link])
#
#         except Exception as e:
#             print("Some elements are missing in this job listing.")
#             print(f"Error details: {e}")
#
# # Close the browser
# driver.quit()
# print(f"Job data has been saved to {csv_file}")

#grok code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Set up Selenium WebDriver
service = Service("C:\\Users\\BHARATH\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Naukri's Python Jobs page
driver.get(
    "https://www.naukri.com/python-jobs?k=python&qproductJobSource=2&naukriCampus=true&experience=0&nignbevent_src=jobsearchDeskGNB")

# Wait until the page is loaded and the job listings are available
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper")))

# Extract job details
jobs = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
print(f"Total Jobs Found: {len(jobs)}")

# Create and write to a CSV file
csv_file = "job_listings.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Posted Date", "Job Link"])

    for job in jobs:
        try:
            # Extract Job Title
            title = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]").text.strip()

            # Extract Company Name
            company = job.find_element(By.XPATH, ".//a[contains(@class, 'comp-name')]").text.strip()

            # Extract Job Location
            location = job.find_element(By.XPATH, ".//span[contains(@class,'locWdth')]").text.strip()

            # Extract Posted Date
            try:
                posted_date_element = WebDriverWait(job, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, ".//span[contains(@class, 'job-post-day')]")
                    )
                )
                posted_date = posted_date_element.text.strip()
            except:
                posted_date = "Unknown"  # If it fails, set "Unknown"

            # Extract Job Link
            job_link = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]").get_attribute("href")

            # Print job details to console
            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"Location: {location}")
            print(f"Posted: {posted_date}")
            print(f"Job Link: {job_link}")
            print("-" * 50)

            # Write job details to CSV file
            writer.writerow([title, company, location, posted_date, job_link])

        except Exception as e:
            print("Some elements are missing in this job listing.")
            print(f"Error details: {e}")

# Close the browser
driver.quit()
print(f"Job data has been saved to {csv_file}")
