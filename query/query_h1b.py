from sqlalchemy import create_engine
from create_h1b import Base, H1b
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, and_, func
import pickle
from kafka import KafkaConsumer
from json import loads
import requests
import collections
import time
import pickle
import datetime
from cache_h1b import query_cache, add_cache
time_stamp = datetime.datetime.now()

# find a company position statistic of how likely it is that the company files your h1b
def company_stat(session, company_name, position):
    # convert company name and position to upper, as it is uppercase in the original table
    
    # calculate the number of cases that were certified vs the total number of cases filed by the company
    s = select([func.avg(H1b.case_status == 'CERTIFIED')]).\
    where(and_(H1b.employer_name.like('%' + company_name + '%'),
               H1b.job_title.like('%' + position + '%')))
    try:
        return float(session.execute(s).first()[0])
    except:
        # return zero if nothing is found
        return 0
    
with open('credentials.pkl', 'rb') as f:
    cred = pickle.load(f)

# Create an engine that stores data on Google Cloud
engine = create_engine('mysql+pymysql://' + cred['user'] + ':' + cred['password'] + '@127.0.0.1/' + cred['database'])

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# kafka consumer
consumer2=KafkaConsumer('query',value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer2:
    company = message.value['company']
    jobtitle = message.value['jobtitle']
    uid = message.value['uid']
    # convert company name and position to upper, as it is uppercase in the original table
    company = company.strip().upper()
    jobtitle = jobtitle.strip().upper()
    start = time.time()
    result, cache_existance = query_cache(company, jobtitle)
    print(result)
    # print(company)
    # print the value calculated from the sql query
    if not cache_existance:
	    result = company_stat(session, company_name =company, position = jobtitle) 
	    print(result)
	    yield add_cache(company, jobtitle, result, time_stamp)
    print(' %0.2f sec' %(time.time() - start))

    requests.post('http://localhost:8080/status?uid={}&status={}'.format(uid, result))


