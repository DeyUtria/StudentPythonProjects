def username_generator(first_name, last_name):
    user_name = first_name[:3] + last_name[:4]
    if len(first_name) < 3 or len(last_name) < 4:
        user_name = first_name + last_name
    return user_name
   
print(username_generator("Deywin", "Utr"))