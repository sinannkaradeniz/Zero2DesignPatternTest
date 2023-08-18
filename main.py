name = "Mustafa"

age =25

surname ="Yıldız"

surnames=["Aslan","Yıldız","Turhan","Emik"]

while age < 30:
    if (age % 2):
        print(age)
        
    if surname in surnames:
        print ("Mıstafa'nın Soyadı Geçerli")
        print(surname)
        print(age)
        age+=1

for soyad in surnames:
    print(soyad)
    if (soyad == "Yıldız"):
        print("Mustafa'nın soyadı")
        
    else:
        print("Değil")
