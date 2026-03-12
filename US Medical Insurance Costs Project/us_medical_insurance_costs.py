#U.S Medical Insurance Costs
#In this project, a CSV file with medical insurance costs will be investigated using python fundamentals.
#The goal with this project will be to analyze various attributes within insurance.csv to learn more about the patient information in the file and gain insight into potential use cases for the dataset.

import csv

#Create empty lists for the various attributes in insurance.csv
ages = []
sexes = []
bmis = []
num_of_children = []
smoker_statuses = []
regions = []
insurance_charges = []

#There are no signs of missing data. To store this information, seven empty lists will be created hold each individual column of data from insurance.csv
def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        
        return lst

#look at the data in insurance_csv_dict
load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_of_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')

#Now that all the data from insurance.csv is neatly organized into labeled lists, the analysis can be started.
#There are some operations that can be implemented. To perform these inspections, a class called PatientsInfo has been built out which contains five methods.

class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_of_children, patients_smoker_statuses, patients_regions, patients_insurance_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_of_children = patients_num_of_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_insurance_charges = patients_insurance_charges

#find average age of patients in insurance.csv
    def find_average_age(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        
        average_age = total_age / len(self.patients_ages)
        return ("The average patient age is: " +str(round(average_age, 2)))
    
    #find number of males and females in insurance.csv
    def analyze_sexes(self):
        females = 0
        males = 0

        for sex in self.patients_sexes:
            if sex == 'female':
                females += 1
            elif sex == 'male':
                males += 1
        print("The number of females are: " +str(females))
        print("The number of males are: " +str(males))

#find each unique region patients are from
def unique_regions(self):
    unique_regions = []
    for region in self.patients_regions:
        if region not in unique_regions:
            unique_regions.append(region)
    return unique_regions

#find average yearly medical charges for patients in insurance.csv
def find_average_charges(self):
    total_charges = 0
    for charge in self.patients_insurance_charges:
        total_charges += float(charge)
    average_charges = total_charges / len(self.patients_insurance_charges)
    return ("The average yearly medical insurance charges are: " + str(round(average_charges, 2)))

#create dictionary with all patients information
def create_dictionary(self):
    self.patients_dictionary = {}
    self.patients_dictionary['Age'] = [int(age) for age in self.patients_ages]
    self.patients_dictionary['Sex'] = self.patients_sexes
    self.patients_dictionary['BMI'] = self.patients_bmis
    self.patients_dictionary['Number of Children'] = self.patients_num_of_children
    self.patients_dictionary['Smoker Status'] = self.patients_smoker_status
    self.patients_dictionary['Region'] = self.patients_regions
    self.patients_dictionary['Charges'] = self.patients_insurance_charges
    return self.patients_dictionary

#The next step is to create an instance of the class called patient_info. With this instance, each method can be used to see the results of the analysis.
patient_info = PatientsInfo(ages,sexes,bmis,num_of_children,smoker_statuses,regions,insurance_charges)
print(patient_info.find_average_age())
#The average patient age is: 39.21

patient_info.analyze_sexes()
print(patient_info.analyze_sexes())
#The number of females are: 1324
#The number of males are: 1352

patient_info.unique_regions()
print(patient_info.unique_regions())
#['southwest', 'southeast', 'northwest', 'northeast']

patient_info.find_average_charges()
print(patient_info.find_average_charges())
#The average yearly medical insurance charges are: 13270.42 dollars

patient_info.create_dictionary()
print(patient_info.patients_dictionary)

