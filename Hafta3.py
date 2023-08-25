def pi_organizer (pi):
    if pi == 3.1415:
        print("Doğru")
        return True
    elif pi <=3:
        print("Yanlış ve 3 ten küşük")
        return False
    else:
        print("Not any information")
        return False

def is_capital(city_name,capitals):
    if city_name in capitals:
        print(city_name+"Yes it is!")
        return True
    elif city_name.capitalize() in capitals:
        print(city_name.capitalize()+"yes but not actually")
        return True
    else:
        return False

def my_filter(input,cptls):
    if isinstance(input,str):
        out = is_capital(input,capitals=cptls)
    else:
        out = pi_organizer(input)
    return out



capitals = ["Seul","Berlin", "Tokyo"]

inputs =["istanbul",2, 64, 22,"berlin", 3.1415,"tokyo", 85, 3, 2, 3,"seul"]
for input in inputs:
    output = my_filter(input,capitals)
    print(output)
   
