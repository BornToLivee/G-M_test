import logging
import os

import requests
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from driver_setup import setup_driver
from utils import slow_typing

logging.basicConfig(filename='out.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

username = os.getenv("LIN_USERNAME")
password = os.getenv("LIN_PASSWORD")

def login_to_linkedin(driver, username, password):
    logging.info("Open login page in LinkedIn")
    driver.get("https://www.linkedin.com/login")
    
    logging.info("Username input")
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    slow_typing(username_field, username)
    
    logging.info("Username input")
    password_field = driver.find_element(By.ID, "password")
    slow_typing(password_field, password)
    password_field.send_keys(Keys.RETURN)

def check_captcha(driver):
    logging.info("Ckecking for CAPTCHA")
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha")))
        logging.warning("CAPTCHA detected, waiting for user input...")
        input("Press Enter to continue...")
    except TimeoutException:
        logging.info("Captcha not detected, continuing...")

def download_profile_photo(driver):
    logging.info("Extraction of photo profile URL")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "feed-identity-module__member-photo")))
    profile_photo_url = driver.find_element(By.CLASS_NAME, "feed-identity-module__member-photo").get_attribute("src")
    
    if profile_photo_url:
        logging.info(f"Photo profile URL: {profile_photo_url}")
        try:
            response = requests.get(profile_photo_url, stream=True)
            response.raise_for_status()

            with open('profile_photo.png', 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            logging.info("Photo saved as profile_photo.png")
        except Exception as e:
            logging.error(f"Unable to download photo: {e}")
    else:
        logging.warning("Photo URL not found")

def main():
    driver = setup_driver()
    
    try:
        login_to_linkedin(driver, username, password)
        check_captcha(driver)
        download_profile_photo(driver)
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
    finally:
        driver.close()
        logging.info("Browsers closed")

if __name__ == "__main__":
    main()