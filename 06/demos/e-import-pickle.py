## Read PICKLE file using Pickle and pandas libraries

# Import pickle files using the pickle library
import pickle
with open('samples\\posts-100.pkl.gz', 'rb') as pickle_file:
    posts_pickle = pickle.load(pickle_file)
print(type(posts_pickle))
print(posts_pickle.columns)
print(posts_pickle.head())

# Import using pandas
import pandas as pd
posts_pickle = pd.read_pickle('samples\\posts-100.pkl')
type(posts_pickle)
print(posts_pickle.columns)
print(posts_pickle.head())

