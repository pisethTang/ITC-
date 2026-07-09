"""
Data Cleaning
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # Import crucial libraries for plotting and exploring data

import numpy as np
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


# <p>Moreover, the link to the Airline data set already contains a test.csv and train.csv set which is not normally the case. Beacause
# a dataset usually comes on its own and it will be split once we get to the Data Analysis stage, where identifying a model for predictions/classfications requires the data to be split into a training and a test set. So to solve this problem we will merge the train and test set together using the pd.concat() </p>
#
# <h3>For good practice, we normally replace whitespace character in columns' names with '_'</h3>

Training_Data = pd.read_csv('train.csv', encoding = 'utf-8')
Training_Data.columns = Training_Data.columns.str.replace(' ', '_')

Testing_Data = pd.read_csv('test.csv', encoding = 'utf-8')
Testing_Data.columns = Testing_Data.columns.str.replace(' ', '_')

Full_Set = pd.concat([Training_Data, Testing_Data]).reset_index(drop=True)


# ## Execute the code below to create a csv file named output.csv containing all the data.

Full_Set.to_csv('output.csv', index=False)


# <h4>We will refer to the the 'Training_Data' and 'Testing_Data' later on when we reach the model identification process.
# For now, we'll use 'Full_Set' data for EDA.</h4>

Full_Set
Full_Set.head()


Full_Set.tail()


# # Understanding the data

Full_Set.shape


Full_Set.columns


Full_Set.info()


# ### Dropping the first column

Full_Set.drop('Unnamed:_0', axis=1, inplace=True)


Full_Set.columns


# # Repeat the above processes again to check that we've removed the 'Unnamed:_0' column

Full_Set.info()


Full_Set.dtypes


# # Checking for percentages of missing values inside each feature

data_with_nan = [features for features in Full_Set.columns if Full_Set[features].isnull().sum]
for feature in data_with_nan:
    print(feature, np.round(Full_Set[feature].isnull().mean(), 4), '% missing values')


# # Fill missing value with mean value

data = Full_Set.fillna({'Arrival_Delay_in_Minutes' : np.min(Full_Set['Arrival_Delay_in_Minutes'])})
for feature in data_with_nan:
    print(feature, np.round(data[feature].isnull().mean(), 4), '% missing values')


# # Checking for outliers

def detect_outlier(data_set):
    outlier_lst = []
    q1 = data_set.quantile(0.25)
    q3 = data_set.quantile(0.75)
    
    IQR = q3 - q1
    
    lower_bound = q1 - 1.5 * IQR
    upper_bound = q3 + 1.5 * IQR
    
    upper_outliers_index = data_set[data_set > upper_bound].index.tolist()
    lower_outliers_index = data_set[data_set < lower_bound].index.tolist()
    
#     upper_outliers = data_set[data_set > upper_bound].tolist()
#     lower_outliers = data_set[data_set < lower_bound]
    
    print(f'Outliers Index: ', upper_outliers_index)

print(detect_outlier(data['Flight_Distance']))


data.head()


data.to_csv('eda_done.csv',index=True)





