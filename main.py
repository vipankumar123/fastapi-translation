from fastapi import FastAPI, Depends, Request, Form, UploadFile, File
from sqlalchemy.orm import Session
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import models
import schemas
from database import engine, SessionLocal
from starlette.templating import Jinja2Templates

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@app.post("/")
def process_form(request: Request, user_input: str = Form(default=''), file_input: UploadFile = File(...)):
    print(f"User input: {user_input}")
    user_input_value = user_input
    
    # Read the content of the uploaded file
    file_content = file_input.file.read().decode("utf-8")
    print("fi;e", file_content)
    return templates.TemplateResponse('index.html', {"request": request, "user_input_value": user_input_value, "file_content": file_content})

# @app.get("/scrapp/data")
# def scrapping_data(db: Session = Depends(get_db)):
#     options = Options()
#     options.add_argument("start-maximized")
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#     driver.implicitly_wait(15)

#     try:
#         driver.get('https://suitecrmdemo.dtbc.eu/index.php')

#         driver.find_element("name", "login_language").click()
#         driver.find_element("xpath", "//*[@id='form']/div[2]/select/option[1]").click()

#         sleep(2)

#         username = driver.find_element("name",'user_name')
#         sleep(2)
#         username.send_keys('Demo')
#         password = driver.find_element("name",'username_password')
#         password.send_keys('Demo')
#         sleep(2)
#         driver.find_element("xpath",'//*[@id="bigbutton"]').click()
#         sleep(3)
#         driver.find_element("xpath", "/html/body/div[2]/nav/div/div[2]/ul/li[3]/span[2]/a").click()
#         driver.get("https://suitecrmdemo.dtbc.eu/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DContacts%26action%3Dindex%26parentTab%3DMarketing")
#         sleep(3)
#         first_20_elements = driver.find_elements("xpath", "//span[@class='suitepicon suitepicon-action-edit']")
#         sleep(2)
#         for i in range(0, 20):
#             first_20_elements = driver.find_elements("xpath", "//span[@class='suitepicon suitepicon-action-edit']")
#             sleep(2)
#             first_20_elements[i].click()
#             sleep(3)
#             first_name = driver.find_element("xpath", "//*[@id='first_name']")
#             last_name = driver.find_element("xpath", "//*[@id='last_name']")
#             phone_number = driver.find_element("xpath", "//*[@id='phone_work']")

#             lead_data = schemas.LeadSchema(
#                 first_name=first_name.get_attribute("value"),
#                 last_name=last_name.get_attribute("value"),
#                 work_phone=phone_number.get_attribute("value")
#             )

#             print("first name:", lead_data.first_name)
#             print("last name:", lead_data.last_name)
#             print("work phone:", lead_data.work_phone)

#             # Call the leads_data function to store the lead data in the database
#             store_lead_data(db, lead_data)

#             sleep(1)
#             driver.back()  # Go back to the previous page
#             sleep(4)
#             if i == 19:
#                 print("2--------")
#                 driver.find_element("xpath", "//*[@id='dtbc-contact-panel']/div/div[1]/div[1]").click()
#                 sleep(2)
#                 driver.find_element("xpath", "/html/body/div[4]/div/div[3]/form[2]/div[3]/table/thead/tr[2]/td/table/tbody/tr/td[4]/button[1]/span").click()
#                 sleep(3)

#         return "Login successful"
#     finally:
#         driver.quit()

# def store_lead_data(db: Session, lead_data: schemas.LeadSchema):
#     new_lead = models.Leads(
#         first_name=lead_data.first_name,
#         last_name=lead_data.last_name,
#         work_phone=lead_data.work_phone
#     )
#     db.add(new_lead)
#     db.commit()
#     db.refresh(new_lead)
