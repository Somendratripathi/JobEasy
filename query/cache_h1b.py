import pickle

def query_cache(company_name, job_title):
	with open(r"./cache.pkl", "rb") as input_file:
			cache = pickle.load(input_file)
	print(cache)

	try:
		score = cache[company_name+':'+job_title]
		return score, True
	except KeyError as e:
		return 0, False

def add_cache(company_name, job_title):
	pass

def add_query(company_name, job_title, score):
	pass

