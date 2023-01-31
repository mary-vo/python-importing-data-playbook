# Import matlab files using scipy.io
import scipy.io
posts_mat = scipy.io.loadmat('samples\\posts-100.mat')
print(type(posts_mat))
# Look at keys and find post which has our data
print(posts_mat.keys())
# Print type 
print(type(posts_mat['posts']))
# Read the dictionary
print(posts_mat['posts'])
