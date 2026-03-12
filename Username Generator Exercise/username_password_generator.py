def username_generator(first_name, last_name):
    user_name = first_name[:3] + last_name[:4]
    if len(first_name) < 3 or len(last_name) < 4:
        user_name = first_name + last_name
    return user_name
   
print(username_generator("Deywin", "UtriaParra"))

def password_generator(user_name):
  password = []
  for i in range(len(user_name[-1])):
    password = user_name[-1] + user_name[:-1]
  return password
print(password_generator("apple"))