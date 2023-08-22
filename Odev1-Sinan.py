InnovationEnabler_TeamName=["Murat", "İlçin", "Sinan", "Beste", "Alara", "Melike"]
YasSıralaması=["Murat", "İlçin", "Sinan", "Beste", "Alara", "Melike"]
InnovationEnabler_TeamAge=[30, 24, 27, 26, 21, 28]
age=20
count=0
while age < (max(InnovationEnabler_TeamAge)+1):
    age+=1
    if age in InnovationEnabler_TeamAge:
        index=InnovationEnabler_TeamAge.index(age)
        YasSıralaması[count]=InnovationEnabler_TeamName[index]
        count+=1


