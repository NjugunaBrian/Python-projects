import re
import pdfplumber
from docx import Document
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def extract_resume_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''

        for page in pdf.pages:
            text += page.extract_text()
    return extract_resume_data(text)


def extract_resume_from_docx(docx_path):
    doc = Document(docx_path)
    text = '\n'.join([para.text for para in doc.paragraphs])

    return extract_resume_data(text)

def extract_resume_data(text):
    resume_data = {}

    resume_data["name"] = text.split('\n')[0]

    #extract email
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    email_match  = re.search(email_pattern, text)
    resume_data["email"] = email_match.group() if email_match else None

    #extract phone number
    phone_pattern = r'(\+?\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}'
    phone_match  = re.search(phone_pattern, text)
    resume_data["phone"] = phone_match.group() if phone_match else None

    return resume_data


def fill_with_resume_data(driver, resume_info):
    time.sleep(3)

    if resume_info['name']:
        name_field = driver.find_element(By.ID, "name")
        name_field.send_keys(resume_info["name"])

    if resume_info['email']:
        name_field = driver.find_element(By.ID, "email")
        name_field.send_keys(resume_info["email"])

    if resume_info['phone']:
        name_field = driver.find_element(By.ID, "phone")
        name_field.send_keys(resume_info["phone"])

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()


    time.sleep(5)

def main(resume_path):

    if resume_path.endswith(".pdf"):
        resume_info = extract_resume_from_pdf(resume_path)
    elif resume_path.endswith(".docx"):
        resume_info = extract_resume_from_docx(resume_path)
    else:
        print("Unsupported file format. Please upload a pdf or Word (.docx) resume")

    print("Extracted Resume Information:", resume_info)


    driver = webdriver.Chrome(executable_path="C:\Users\admin\selenium-driver\chrome-win64\chrome.exe")

    driver.get("https://example.com/form")

    fill_with_resume_data(driver, resume_info)

    driver.quit

if __name__  == "__main__":

    resume_path = "C:\Users\admin\Documents\Curriculum Vitaes\Brian Njuguna Resume.docx"

    if os.path.exists(resume_path):
        main(resume_path)
    else:
        print(f"File {resume_path} not found!")    
  


            

    
   
