# 1st code
# from flask import Flask, render_template, request, send_from_directory
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import re
#
# app = Flask(__name__, static_folder="static")
#
# # Function to parse experience range (e.g., "0-2 Yrs" -> [0, 2])
# def parse_experience(exp_str):
#     if not exp_str or "Not Mentioned" in exp_str.lower():
#         return [0, 0]  # Default to 0-0 for unmentioned experience
#     # Extract numbers from the string (e.g., "0-2 Yrs" -> [0, 2])
#     numbers = re.findall(r'\d+', exp_str)
#     if len(numbers) == 2:
#         return [int(numbers[0]), int(numbers[1])]  # Return [min, max]
#     elif len(numbers) == 1:
#         return [int(numbers[0]), int(numbers[0])]  # Single value, e.g., "5 Yrs"
#     return [0, 0]  # Fallback
#
# # Function to scrape job data
# def scrape_jobs(role, location, experience):
#     job_list = []
#
#     # Adjust experience parameter for freshers or range
#     if int(experience) == 0:
#         experience_param = "0"  # Try "0" for freshers
#     else:
#         experience_param = f"0-{experience}"  # Range for non-zero experience
#
#     service = Service("C:\\Users\\BHARATH\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#
#     # Generate search URL
#     search_url = f"https://www.naukri.com/{role.replace(' ', '-')}-jobs?k={role}&l={location}&experience={experience_param}"
#     driver.get(search_url)
#
#     try:
#         # Wait for job listings to load
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper")))
#
#         jobs = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
#
#         for job in jobs:
#             try:
#                 title_element = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]")
#                 title = title_element.text.strip()
#                 job_link = title_element.get_attribute("href")
#
#                 company = job.find_element(By.XPATH, ".//a[contains(@class, 'comp-name')]").text.strip()
#                 location = job.find_element(By.XPATH, ".//span[contains(@class,'locWdth')]").text.strip()
#
#                 # Extract experience details properly
#                 try:
#                     experience_text = job.find_element(By.XPATH, ".//span[contains(@class, 'exp')]").text.strip()
#                 except:
#                     experience_text = "Not Mentioned"
#
#                 job_list.append({
#                     "title": title,
#                     "company": company,
#                     "location": location,
#                     "experience": experience_text,
#                     "link": job_link
#                 })
#
#             except Exception as e:
#                 print(f"Error extracting job details: {e}")
#
#     except Exception as e:
#         print("Error loading job listings:", e)
#
#     driver.quit()
#     return job_list
#
# # Flask route to render UI
# @app.route("/", methods=["GET", "POST"])
# def index():
#     jobs = []
#     if request.method == "POST":
#         role = request.form["role"]
#         location = request.form["location"]
#         experience = request.form["experience"]
#         jobs = scrape_jobs(role, location, experience)
#
#         # Post-scraping filter for exact experience match
#         if int(experience) == 0:
#             jobs = [job for job in jobs if parse_experience(job["experience"])[0] == 0]
#         else:
#             jobs = [job for job in jobs if parse_experience(job["experience"])[1] >= int(experience)]
#
#     return render_template("index.html", jobs=jobs)
#
# # Serve static files manually (if CSS is not loading)
# @app.route('/static/<path:filename>')
# def static_files(filename):
#     return send_from_directory(os.path.join(app.root_path, 'static'), filename)
#
# if __name__ == "__main__":
#     app.run(debug=True)

# #2nd code
# from flask import Flask, render_template, request, send_from_directory
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import re
#
# app = Flask(__name__, static_folder="static")
#
# # Function to parse experience range (e.g., "0-2 Yrs" -> [0, 2])
# def parse_experience(exp_str):
#     if not exp_str or "Not Mentioned" in exp_str.lower():
#         return [0, 0]  # Default to 0-0 for unmentioned experience
#     # Extract numbers from the string (e.g., "0-2 Yrs" -> [0, 2])
#     numbers = re.findall(r'\d+', exp_str)
#     if len(numbers) == 2:
#         return [int(numbers[0]), int(numbers[1])]  # Return [min, max]
#     elif len(numbers) == 1:
#         return [int(numbers[0]), int(numbers[0])]  # Single value, e.g., "5 Yrs"
#     return [0, 0]  # Fallback
#
# # Function to scrape job data for a single role
# def scrape_jobs(role, location, experience):
#     job_list = []
#
#     # Adjust experience parameter for freshers or range
#     if int(experience) == 0:
#         experience_param = "0"  # Try "0" for freshers
#     else:
#         experience_param = f"0-{experience}"  # Range for non-zero experience
#
#     service = Service("C:\\Users\\BHARATH\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#
#     # Generate search URL
#     search_url = f"https://www.naukri.com/{role.replace(' ', '-')}-jobs?k={role}&l={location}&experience={experience_param}"
#     driver.get(search_url)
#
#     try:
#         # Wait for job listings to load
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper")))
#
#         jobs = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
#
#         for job in jobs:
#             try:
#                 title_element = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]")
#                 title = title_element.text.strip()
#                 job_link = title_element.get_attribute("href")
#
#                 company = job.find_element(By.XPATH, ".//a[contains(@class, 'comp-name')]").text.strip()
#                 location = job.find_element(By.XPATH, ".//span[contains(@class,'locWdth')]").text.strip()
#
#                 # Extract experience details properly
#                 try:
#                     experience_text = job.find_element(By.XPATH, ".//span[contains(@class, 'exp')]").text.strip()
#                 except:
#                     experience_text = "Not Mentioned"
#
#                 job_list.append({
#                     "title": title,
#                     "company": company,
#                     "location": location,
#                     "experience": experience_text,
#                     "link": job_link
#                 })
#
#             except Exception as e:
#                 print(f"Error extracting job details: {e}")
#
#     except Exception as e:
#         print("Error loading job listings:", e)
#
#     driver.quit()
#     return job_list
#
# # Flask route to render UI
# @app.route("/", methods=["GET", "POST"])
# def index():
#     jobs = []
#     if request.method == "POST":
#         role = request.form["role"]
#         location = request.form["location"]
#         experience = request.form["experience"]
#
#         # Split the role input into multiple keywords
#         keywords = [kw.strip() for kw in role.split(',') if kw.strip()]
#         all_jobs = []
#
#         # Scrape jobs for each keyword
#         for keyword in keywords:
#             if keyword:  # Ensure keyword is not empty
#                 keyword_jobs = scrape_jobs(keyword, location, experience)
#                 all_jobs.extend(keyword_jobs)
#
#         # Remove duplicates based on job link
#         seen_links = set()
#         jobs = [job for job in all_jobs if job["link"] not in seen_links and not seen_links.add(job["link"])]
#
#         # Post-scraping filter for exact experience match
#         if int(experience) == 0:
#             jobs = [job for job in jobs if parse_experience(job["experience"])[0] == 0]
#         else:
#             jobs = [job for job in jobs if parse_experience(job["experience"])[1] >= int(experience)]
#
#     return render_template("index.html", jobs=jobs)
#
# # Serve static files manually (if CSS is not loading)
# @app.route('/static/<path:filename>')
# def static_files(filename):
#     return send_from_directory(os.path.join(app.root_path, 'static'), filename)
#
# if __name__ == "__main__":
#     app.run(debug=True)

#3rd good code
# from flask import Flask, render_template, request, send_from_directory
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import re
#
# app = Flask(__name__, static_folder="static")
#
# # Function to parse experience range (e.g., "0-2 Yrs" -> [0, 2])
# def parse_experience(exp_str):
#     if not exp_str or "Not Mentioned" in exp_str.lower():
#         return [0, 0]  # Default to 0-0 for unmentioned experience
#     # Extract numbers from the string (e.g., "0-2 Yrs" -> [0, 2])
#     numbers = re.findall(r'\d+', exp_str)
#     if len(numbers) == 2:
#         return [int(numbers[0]), int(numbers[1])]  # Return [min, max]
#     elif len(numbers) == 1:
#         return [int(numbers[0]), int(numbers[0])]  # Single value, e.g., "5 Yrs"
#     return [0, 0]  # Fallback
#
# # Function to scrape job data for a single role/skill
# def scrape_jobs(role, location, experience):
#     job_list = []
#
#     # Adjust experience parameter for freshers or range
#     if int(experience) == 0:
#         experience_param = "0"  # Try "0" for freshers
#     else:
#         experience_param = f"0-{experience}"  # Range for non-zero experience
#
#     service = Service("C:\\Users\\BHARATH\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#
#     # Generate search URL
#     search_url = f"https://www.naukri.com/{role.replace(' ', '-')}-jobs?k={role}&l={location}&experience={experience_param}"
#     driver.get(search_url)
#
#     try:
#         # Wait for job listings to load
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper")))
#
#         jobs = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
#
#         for job in jobs:
#             try:
#                 title_element = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]")
#                 title = title_element.text.strip().lower()
#                 job_link = title_element.get_attribute("href")
#
#                 company = job.find_element(By.XPATH, ".//a[contains(@class, 'comp-name')]").text.strip()
#                 location = job.find_element(By.XPATH, ".//span[contains(@class,'locWdth')]").text.strip()
#
#                 # Extract experience details properly
#                 try:
#                     experience_text = job.find_element(By.XPATH, ".//span[contains(@class, 'exp')]").text.strip()
#                 except:
#                     experience_text = "Not Mentioned"
#
#                 job_list.append({
#                     "title": title,
#                     "company": company,
#                     "location": location,
#                     "experience": experience_text,
#                     "link": job_link
#                 })
#
#             except Exception as e:
#                 print(f"Error extracting job details: {e}")
#
#     except Exception as e:
#         print("Error loading job listings:", e)
#
#     driver.quit()
#     return job_list
#
# # Flask route to render UI
# @app.route("/", methods=["GET", "POST"])
# def index():
#     jobs = []
#     if request.method == "POST":
#         role = request.form["role"]
#         location = request.form["location"]
#         experience = request.form["experience"]
#
#         # Split the role input into multiple skills
#         skills = [skill.strip().lower() for skill in role.split(',') if skill.strip()]
#         all_jobs = []
#
#         # Scrape jobs for each skill
#         for skill in skills:
#             if skill:  # Ensure skill is not empty
#                 skill_jobs = scrape_jobs(skill, location, experience)
#                 all_jobs.extend(skill_jobs)
#
#         # Remove duplicates based on job link
#         seen_links = set()
#         jobs = [job for job in all_jobs if job["link"] not in seen_links and not seen_links.add(job["link"])]
#
#         # Post-scraping filter for exact experience match
#         if int(experience) == 0:
#             jobs = [job for job in jobs if parse_experience(job["experience"])[0] == 0]
#         else:
#             jobs = [job for job in jobs if parse_experience(job["experience"])[1] >= int(experience)]
#
#         # Enhance combination detection by tagging jobs with matched skills
#         for job in jobs:
#             job["matched_skills"] = [skill for skill in skills if skill in job["title"]]
#
#     return render_template("index.html", jobs=jobs)
#
# # Serve static files manually (if CSS is not loading)
# @app.route('/static/<path:filename>')
# def static_files(filename):
#     return send_from_directory(os.path.join(app.root_path, 'static'), filename)
#
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, send_from_directory
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re
import time

app = Flask(__name__, static_folder="static")

# Function to parse experience range (e.g., "0-2 Yrs" -> [0, 2])
def parse_experience(exp_str):
    if not exp_str or "Not Mentioned" in exp_str.lower():
        return [0, 0]
    numbers = re.findall(r'\d+', exp_str)
    if len(numbers) == 2:
        return [int(numbers[0]), int(numbers[1])]
    elif len(numbers) == 1:
        return [int(numbers[0]), int(numbers[0])]
    return [0, 0]

# Function to scrape job data and key skills for a single role/skill
def scrape_jobs(role, location, experience, max_jobs=5):
    job_list = []

    if int(experience) == 0:
        experience_param = "0"
    else:
        experience_param = f"0-{experience}"

    service = Service("C:\\Users\\BHARATH\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    search_url = f"https://www.naukri.com/{role.replace(' ', '-')}-jobs?k={role}&l={location}&experience={experience_param}"
    print(f"Searching URL: {search_url}")
    driver.get(search_url)

    try:
        # Wait for job listings to load and collect all job links first
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper")))
        job_elements = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")[:max_jobs]
        job_links = [job.find_element(By.XPATH, ".//a[contains(@class, 'title')]").get_attribute("href") for job in job_elements]

        for link in job_links:
            try:
                print(f"Processing job link: {link}")
                driver.get(link)
                time.sleep(5)  # Increased wait to ensure page loads fully

                # Extract details from job detail page
                try:
                    title_element = driver.find_element(By.XPATH, "//h1[contains(@class, 'jd-job-title')]")
                    title = title_element.text.strip().lower()
                except:
                    title = "Unknown Title"
                    print("Failed to extract title")

                try:
                    company_element = driver.find_element(By.XPATH, "//div[contains(@class, 'job-details')]//a[contains(@class, 'comp-name')]")
                    company = company_element.text.strip()
                except:
                    company = "Unknown Company"
                    print("Failed to extract company")

                try:
                    location_element = driver.find_element(By.XPATH, "//span[contains(@class, 'loc')]")
                    location = location_element.text.strip()
                except:
                    location = "Unknown Location"
                    print("Failed to extract location")

                try:
                    experience_element = driver.find_element(By.XPATH, "//span[contains(@class, 'exp')]")
                    experience_text = experience_element.text.strip()
                except:
                    experience_text = "Not Mentioned"
                    print("Failed to extract experience")

                # Extract key skills with retry
                key_skills = []
                preferred_skills = []
                for attempt in range(3):  # Retry up to 3 times
                    try:
                        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'styles_key-skill__GIPn')]")))
                        key_skills_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'styles_key-skill__GIPn')]")
                        key_skills = [skill.text.strip().lower().replace('☆', '').replace('★', '').strip() for skill in key_skills_elements if skill.text.strip()]
                        preferred_skills = [skill.text.strip().lower().replace('☆', '').replace('★', '').strip() for skill in key_skills_elements if '☆' in skill.text or '★' in skill.text or 'preferred' in skill.text.lower()]
                        if key_skills:
                            break
                    except Exception as e:
                        print(f"Attempt {attempt + 1} failed to load key skills for {link}: {e}")
                        time.sleep(2)
                        if attempt == 2:
                            print(f"Failed to load key skills after 3 attempts for {link}")

                print(f"Found job: {title}, Company: {company}, Location: {location}, Experience: {experience_text}, Key Skills: {key_skills}, Preferred Skills: {preferred_skills}")
                job_list.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "experience": experience_text,
                    "link": link,
                    "key_skills": key_skills,
                    "preferred_skills": preferred_skills
                })

            except Exception as e:
                print(f"Error processing job {link}: {e}")

    except Exception as e:
        print("Error loading job listings:", e)

    driver.quit()
    return job_list

# Flask route to render UI
@app.route("/", methods=["GET", "POST"])
def index():
    jobs = []
    if request.method == "POST":
        role = request.form["role"]
        location = request.form["location"]
        experience = request.form["experience"]

        # Split the role input into multiple skills
        skills = [skill.strip().lower() for skill in role.split(',') if skill.strip()]
        all_jobs = []

        # Scrape jobs for each skill with a delay to avoid rate limiting
        for skill in skills:
            if skill:
                print(f"Scraping jobs for skill: {skill}")
                skill_jobs = scrape_jobs(skill, location, experience, max_jobs=5)
                all_jobs.extend(skill_jobs)
                time.sleep(3)  # Increased delay

        # Remove duplicates based on job link
        seen_links = set()
        jobs = [job for job in all_jobs if job["link"] not in seen_links and not seen_links.add(job["link"])]

        # Post-scraping filter for exact experience match
        if int(experience) == 0:
            jobs = [job for job in jobs if parse_experience(job["experience"])[0] == 0]
        else:
            jobs = [job for job in jobs if parse_experience(job["experience"])[1] >= int(experience)]

        # Tag jobs with matched skills
        for job in jobs:
            job["matched_skills"] = [skill for skill in skills if any(s in ' '.join(job["key_skills"]) for s in [skill])]

    return render_template("index.html", jobs=jobs)

# Serve static files manually (if CSS is not loading)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == "__main__":
    app.run(debug=True)