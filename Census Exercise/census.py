# Import pandas with alias
import pandas as pd


# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
print(census.head(5))

#The manager of the census would like to know the average birth year of the respondents. We were able to see from .dtypes that birth_year has been assigned the str datatype whereas it should be expressed in int. Print the unique values of the variable using the .unique() method.
print(census.dtypes)
print(census['birth_year'].unique())

#There appears to be a missing value in the birth_year column. With some research you find that the respondent’s birth year is 1967. Use the .replace() method to replace the missing value with 1967, so that the data type can be changed to int. Then recheck the values in birth_year by calling the .unique() method and printing the results.
census['birth_year'] = census['birth_year'].replace(['missing'], 1967)
print(census['birth_year'].unique())

#Now that we have adjusted the values in the birth_year variable, change the datatype from str to int and print the datatypes of the census dataframe with .dtypes.
census['birth_year'] = census['birth_year'].astype('int')
print(census.dtypes)

#Having assigned birth_year to the appropriate data type, print the average birth year of the respondents to the census using the pandas .mean() method.
print(census['birth_year'].mean())

#Your manager would like to set an order to the higher_tax variable so that: strongly disagree < disagree < neutral < agree < strongly agree. Convert the higher_tax variable to the category data type with the appropriate order, then print the new order using the .unique() method.
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)
print(census['higher_tax'].unique())

#Your manager would also like to know the median sentiment of the respondents on the issue of higher taxes for the wealthy. Label encode the higher_tax variable and print the median using the pandas .median() method.
census['higher_tax'] = census['higher_tax'].cat.codes
print(census['higher_tax'].median())

#If you plan to reuse the original `marital_status` column for label encoding, consider making a copy before one-hot encoding, as get_dummies will remove it. census['marital_status_copy'] = census['marital_status']
census = pd.get_dummies(data=census, columns = ['marital_status'])
print(census.head(5))

#Create a new variable called marital_codes by Label Encoding the marital_status variable. This could help the Census team use machine learning to predict if a respondent thinks the wealthy should pay higher taxes based on their marital status.
census['marital_codes'] = pd.Categorical(census['marital_status'])
bins = range(census['birth_year'].min(), census['birth_year'].max() + 5, 5)

#Create a new variable called age_group, which groups respondents based on their birth year. The groups should be in five-year increments, e.g., 25-30, 31-35, etc. Then label encode the age_group variable to assist the Census team in the event they would like to use machine learning to predict if a respondent thinks the wealthy should pay higher taxes based on their age group.
census['age_group'] = pd.cut(census['birth_year'], bins=bins)
census['age_group_code'] = pd.Categorical(census['age_group']).co