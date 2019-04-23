from sqlalchemy import create_engine
from create_h1b import Base, H1b
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, and_, func
import pickle

def company_stat(session, company_name, position):
    company_name = company_name.upper()
    position = position.upper()
    
    s = select([func.avg(H1b.case_status == 'CERTIFIED')]).\
    where(and_(H1b.employer_name.like('%' + company_name + '%'),
               H1b.job_title.like('%' + position + '%')))
    try:
        return float(session.execute(s).first()[0])
    except:
        return 0
    
with open('credentials.pkl', 'rb') as f:
    cred = pickle.load(f)

engine = create_engine('mysql+pymysql://' + cred['user'] + ':' + cred['password'] + '@127.0.0.1/' + cred['database'])
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

print(company_stat(session, company_name = 'Google', position = 'Software Engineer'))

