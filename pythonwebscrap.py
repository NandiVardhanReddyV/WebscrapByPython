from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Set up Selenium WebDriver
#service = Service("C:\\Users\\BHARATH\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")  # Your chromedriver path
service = Service("C:\\Users\\BHARATH\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Naukri's Python Jobs page
driver.get("https://www.naukri.com/python-jobs?k=python&qproductJobSource=2&naukriCampus=true&experience=0&nignbevent_src=jobsearchDeskGNB")

# Wait until the page is loaded and the job listings are available
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper")))

# Extract job details
jobs = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
print(f"Total Jobs Found: {len(jobs)}")

# Create and write to a CSV file
csv_file = "job_listings.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location"])  # Header row

    for job in jobs:
        try:
            # Adjusted XPath selectors (you may need to inspect elements and adjust based on actual structure)
            title = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]").text.strip()
            company = job.find_element(By.XPATH, ".//a[contains(@class, 'comp-name')]").text.strip()
            location = job.find_element(By.XPATH, ".//span[contains(@class,'locWdth')]").text.strip()

            # Print job details to console
            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"Location: {location}")
            print("-" * 50)

            # Write job details to CSV file
            writer.writerow([title, company, location])

        except Exception as e:
            print("Some elements are missing in this job listing.")
            print(f"Error details: {e}")

# Close the browser
driver.quit()
print(f"Job data has been saved to {csv_file}")
