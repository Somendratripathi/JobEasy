import pickle

cache = dict()
with open(r"./cache.pkl", "rb") as input_file:
		cache = pickle.load(input_file)
print(cache)