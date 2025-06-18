import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def scrape_website(website):
    print("Lauching browser...")

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print(f"Scraping data from: {website}")
        html = driver.page_source

        time.sleep(10)  # Wait for the page to load completely

        return html
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("Browser closed.")

def extract_data(html):
    # Placeholder for data extraction logic
    # This function would parse the HTML and extract the required data
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str (body_content)
    else:
        return ""
    return html 

def clean_body(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()
    
    cleaned = soup.get_text(separator='\n')
    cleaned = "\n".join(line.strip() for line in cleaned.splitlines() if line.strip())

    return cleaned

def split_text(text, max_length=6000):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

