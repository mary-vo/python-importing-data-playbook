## You can read SAS files using sas7bdat or pandas

# Import sas7bdat using sas7bdat 
from sas7bdat import SAS7BDAT
# Use context manager
with SAS7BDAT('samples\\posts-100.sas7bdat') as sas_file:    
	users_sas_df = sas_file.to_data_frame()
dir(sas_file)
print(sas_file.column_names)
print(sas_file.header)
print(type(users_sas_df))

# Using pandas
import pandas as pd
posts_sas = pd.read_sas('samples\\posts-100.sas7bdat')
print(type(posts_sas))
# See the first few records
print(posts_sas.head())
# See the columns
print(posts_sas.columns)
# In case the file is large, we can use chunksize parameter which allows me to get the number of records indicated by chunksize
posts_sas_reader = pd.read_sas('samples\\posts-100.sas7bdat', chunksize=3)
print(posts_sas_reader.read())

