import time
import random
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


catchall_domain = input("Enter the catchall domain (e.g., example.com): ")
num_runs = int(input("How many times would you like to run this script? "))

options = ChromeOptions()
options.headless = False  # Set headless to False to show the browser
driver = Chrome(options=options)

url = "https://www.dominosemergencypizzaforstudentloans.com/"#url to generate codes for
driver.get(url)

fake = Faker()

def generate_random_email():#function for making emails with user domain 
    random_string = ''.join(random.choice(
        "abcdefghijklmnopqrstuvwxyz") for _ in range(10))
    return f"{random_string}@{catchall_domain}"

def generate_random_college_name():#needed for the dominos emergency pizza for students program
    colleges = [
        "Harvard University",
        "Stanford University",
        "MIT",
        "University of California, Berkeley",
        "Yale University",
        "Princeton University",
        "Columbia University",
        "University of Chicago",
        "California Institute of Technology",
        "University of Oxford",
        "University of Cambridge",
        "Massachusetts Institute of Technology",
        "Stanford University",
        "University of California, Los Angeles",
    ]
    return random.choice(colleges)


for _ in range(num_runs): #begin generating
    full_name = fake.name()
    email = generate_random_email()
    college_name = generate_random_college_name()
    year_of_graduation = str(random.randint(2023, 2026))

    driver.find_element(By.ID, "FullName").clear()
    driver.find_element(By.ID, "Email").clear()
    driver.find_element(By.ID, "Institution").clear()
    driver.find_element(By.ID, "Year").clear()

    time.sleep(random.uniform(1.0, 2.5))
    driver.find_element(By.ID, "FullName").send_keys(full_name)

    time.sleep(random.uniform(1.0, 2.5))
    driver.find_element(By.ID, "Email").send_keys(email)

    time.sleep(random.uniform(1.0, 2.5))
    driver.find_element(By.ID, "Institution").send_keys(college_name)

    time.sleep(random.uniform(1.0, 2.5))
    driver.find_element(By.ID, "Year").send_keys(year_of_graduation)

    driver.find_element(By.ID, "AffAceptance").click()

    time.sleep(random.uniform(1.0, 2.5))
    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-circle-btn")))
    submit_button.click()

    time.sleep(5 + random.uniform(1.0, 2.5))


time.sleep(random.uniform(1.0, 2.5))
driver.find_element(By.ID, "btn-Enter").click()


driver.quit()