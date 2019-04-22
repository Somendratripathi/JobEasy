import os
import sys
from sqlalchemy import Column, Integer, String, Date, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import pickle

Base = declarative_base()

class H1b(Base):
    __tablename__ = 'H1B_2019'
    # Here we define columns for the H1B person
    # Notice that each column is also a normal Python instance attribute.
    case_number = Column(String(64), primary_key = True)
    case_status = Column(String(128), nullable= False)
    case_submitted = Column(Date, nullable = False)
    decision_date = Column(Date, nullable = False)
    visa_class = Column(String(32), nullable= False)
    employment_start_date = Column(Date, nullable = False)
    employment_end_date = Column(Date)
    employer_name = Column(String(1024))
    employer_business_dba = Column(String(256))
    employer_address = Column(String(2048))
    employer_city = Column(String(128))
    employer_state = Column(String(4))
    employer_country = Column(String(32))
    employer_province = Column(String(128))
    employer_phone = Column(String(16))
    employer_phone_ext = Column(Integer)
    agent_representing_employer = Column(String(2))
    agent_attorney_name = Column(String(1024))
    agent_attorney_city = Column(String(32))
    agent_attorney_state = Column(String(4))
    job_title = Column(String(128))
    soc_code = Column(String(128))
    soc_name = Column(String(128))
    naics_code = Column(Integer)
    total_workers = Column(Integer)
    new_employment = Column(Integer)
    continued_employment = Column(Integer)
    change_previous_employment = Column(Integer)
    new_concurrent_emp = Column(Integer)
    change_employer = Column(Integer)
    amended_petition = Column(Integer)
    full_time_position = Column(String(2))
    prevailing_wage = Column(DECIMAL(15, 3))
    pw_unit_of_pay = Column(String(32))
    pw_wage_level = Column(String(16))
    pw_source = Column(String(8))
    pw_source_year = Column(Integer)
    pw_source_other = Column(String(256))
    wage_rate_of_pay_from = Column(DECIMAL(15, 3))
    wage_rate_of_pay_to = Column(DECIMAL(15, 3))
    wage_unit_of_pay = Column(String(16))
    h1b_dependent = Column(String(2))
    willful_violator = Column(String(2))
    support_h1b = Column(String(4))
    labor_con_agree = Column(String(2))
    public_disclosure_location = Column(String(4))
    worksite_city = Column(String(32))
    worksite_county = Column(String(32))
    worksite_state = Column(String(4))
    worksite_postal_code = Column(String(32))
    original_cert_date = Column(Date)

# Create an engine that stores data on Google Cloud
with open('credentials.pkl', 'rb') as f:
    cred = pickle.load(f)

engine = create_engine('mysql+pymysql://' + cred['user'] + ':' + cred['password'] + '@127.0.0.1/' + cred['database'])
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
