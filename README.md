# Python Job Scraper using Selenium  

This project is a web scraping tool that extracts Python job listings from [Naukri.com](https://www.naukri.com) using **Selenium**. The scraped job details are saved into a CSV file for further analysis.  

## Features  
- Scrapes job titles, company names, locations, and job links.  
- Uses **Selenium WebDriver** to interact with dynamic web pages.  
- Saves the extracted data into a CSV file (`job_listings.csv`).  
- Handles missing elements gracefully with error handling.  

## Technologies Used  
- **Python**  
- **Selenium** for web scraping  
- **CSV module** for data storage  
- **WebDriverWait** for handling dynamic page loads  

## Installation & Setup  
### Prerequisites  
- Install Python (>=3.7)  
- Install Selenium:  
  ```bash
  pip install selenium

  1. **Check your Chrome version**:  
   - Open Chrome → Click on **3 dots (⋮) > Help > About Google Chrome**.  
   - Note the version (e.g., **123.0.6312.122**).  

2. **Download the matching ChromeDriver**:  
   - Go to: [ChromeDriver Site](https://sites.google.com/chromium.org/driver/)  
   - Download the **correct version** for your OS.  

3. **Extract and set the path in the script**:  
   ```python
   from selenium import webdriver
   from selenium.webdriver.chrome.service import Service

   service = Service("C:\\path\\to\\chromedriver.exe")  # Update this path
   driver = webdriver.Chrome(service=service)

