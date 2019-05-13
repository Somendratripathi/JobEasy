from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time
from create_h1b import Base, H1b
from datetime import datetime
import numpy as np
import pandas as pd
import pickle



		

def store_updates(dictionary, timestamp):
	# Create an engine that stores data on Google Cloud
	with open('credentials.pkl', 'rb') as f:
		cred = pickle.load(f)

	engine = create_engine('mysql+pymysql://' + cred['user'] + ':' + cred['password'] + '@127.0.0.1/' + cred['database2'])

	# Bind the engine to the metadata of the Base class so that the
	# declaratives can be accessed through a DBSession instance
	Base.metadata.bind = engine

	DBSession = sessionmaker(bind=engine)
	# A DBSession() instance establishes all conversations with the database
	# and represents a "staging zone" for all the objects loaded into the
	# database session object. Any change made against the objects in the
	# session won't be persisted into the database until you call
	# session.commit(). If you're not happy about the changes, you can
	# revert all of them back to the last commit by calling
	# session.rollback()
	session = DBSession()
	
	select([func.avg(H1b.case_status == 'CERTIFIED')]).\
    where(and_(H1b.employer_name.like('%' + company_name + '%'),
               H1b.job_title.like('%' + position + '%')))
			   
	session.execute(s)
			   
	cache_data = pd.DataFrame(dictionary)
	cache_data.columns = ['case_submitted','decision_date','employment_start_date','employment_end_date','original_cert_date']

	cache_data[parse_dates] = cache_data[parse_dates].astype(str)
	cache_data.replace(to_replace='NaT', value=np.nan, inplace = True)
	cache_data = cache_data.astype(object).where(pd.notnull(cache_data), None)

	start = time.time()
	engine.execute(cache.__table__.insert(),
				   cache_data.to_dict(orient='records'))
	duration = time.time() - start
	print('Insertion into table - total time: {:.2f} seconds'.format(duration))