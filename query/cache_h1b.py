import datetime

#No need for pickling
cache = {}
def query_cache(company_name, job_title):
	#with open(r"./cache.pkl", "rb") as input_file:
	#		cache = pickle.load(input_file)

	#print(cache)
	if cache.get(None,[company_name+':'+job_title]) == None:
		return 0, False
	
	score = cache[company_name+':'+job_title]
	#try:
		
	return score, True
	#except KeyError as e:
	#	return 0, False

def add_cache(company_name, job_title, score, timestamp):
	# current time
	curr_time = datetime.datetime.now()
	# read cache
	#with open(r"./cache.pkl", "rb") as input_file:
	#		cache = pickle.load(input_file)
	# delete cache
	if (curr_time - timestamp).days >= 1:
		cache = {}

	score = cache.get([company_name+':'+job_title], None)

	if score == None: 
		#score does not exist cache it 
		cache[company_name+':'+job_title] = score
		return 1 #success 
	
	return 0 #score exists no need to update

	

	#try:
	#	score = cache[company_name+':'+job_title]
	#	return 0

	#except KeyError as e:
	#	cache[company_name+':'+job_title] = score

	#with open(r"./cache.pkl", "wb") as output_file:
	#	pickle.dump(cache, output_file)

	#return 0


