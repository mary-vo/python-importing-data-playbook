## Read HDF5 files with h5py and pandas librarites

# Import hdf5 using h5py
import h5py
file = h5py.File("samples\\posts-100.h5",'r')
dataset = file['posts']
print(type(dataset))
# Iterate over the data
for x in dataset['table']:
    print(x)

# Using pandas
import pandas as pd
posts_hdf = pd.read_hdf('samples\\posts-100.h5', 'posts')
# Both of these columsn and keys() returns the columns
print(posts_hdf.columns)
print(posts_hdf.keys())
# Start and Stop identifies which rows we want to load; columns identifies the columns we want to load
print(pd.read_hdf('samples\\posts-100.h5', 'posts', start=2, stop=5, columns=['CreationDate','Title','Tags']).head())
# Filtering data using where
print(pd.read_hdf('samples\\posts-100.h5', 'posts', columns=['Score', 'Tags'], where='Score>10 or Tags = "<machine-learning>"').head())
