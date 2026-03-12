# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)


# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name =
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)


# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)


# Estimate Akira's insurance cost
akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)


#Find actual insurance cost data and zip it together with the names and estimated insurance costs into a list of tuples. Then, print the list of tuples.
names = ["Maria", "Rohan", "Valentina"]
names.append("Akira")
insurance_costs = [4150.0, 5320.0, 35210.0]
insurance_costs.append(2930.0)
insurance_data = zip(names, insurance_costs)
converted_list = list(zip(insurance_data))
print("Here's the actual insurance cost data: " + str(converted_list))

#Find estimated insurance cost data and zip it together with the names and print it.
estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
estimated_insurance_data.append(("Akira", akira_insurance_cost))
print("Here's the estimated insurance cost data: " + str(estimated_insurance_data))

#Find the difference between the actual insurance cost and the estimated insurance cost for each person. Zip the names together with the differences and print it as a list of tuples.
maria_difference = [4150.0 - maria_insurance_cost]
rohan_difference = [5320.0 - rohan_insurance_cost]
valentina_difference = [35210.0 - valentina_insurance_cost]
akira_difference = [2930.0 - akira_insurance_cost]


insurance_cost_difference = []
insurance_cost_difference.append(("Maria", maria_difference))
insurance_cost_difference.append(("Rohan", rohan_difference))
insurance_cost_difference.append(("Valentina", valentina_difference))
insurance_cost_difference.append(("Akira", akira_difference))
print("Here's the difference between the actual insurance cost and the estimated insurance cost: " + "" + str(insurance_cost_difference))