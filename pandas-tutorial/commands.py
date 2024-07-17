import numpy as np
import pandas as pd

dict1= {
    "Name":['Rahul', 'Vijay', 'Abhishek', 'Ashish' ],
    "Marks":[92,56,89,47],
    "City":['Rampur', 'Bareilly', 'Kolkata', 'Pune']
}

#Creating Data_Frame

df = pd.DataFrame(dict1)

#Creating a csv file

df.to_csv('first_file')

# remove the indexing from csv file

df.to_csv('file_with_no_index', index=False)

# if you want to see first 2 rows from starting

df.head(2)

# if you want to see first 2 rows from the end

df.tail(2)

# if you want description/statistic analysis of numerical columns such as their count, mean, standard deviation etc etc

df.describe()

#to read a csv file

File=pd.read_csv('File_name.csv')

File

# to read any specific column 

File['Marks']

# to read an element of column from specific index

File['Marks'][0]

# to change an element of column from specific index

File['Marks'][0]=60

# to change the index

File.index=['First', 'Second', 'Third', 'Fourth']
