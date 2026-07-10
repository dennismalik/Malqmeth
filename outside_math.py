#Trial
person_name = "dennis audrey"
rating = 4.99
is_published = True
research_name = "Quantitative Analysis On Dementia Patients"
print(len(research_name))
print(research_name[0])
print(research_name[-3])
print(research_name[0:5])

first = "dennis"
last = "audrey"
full_name= f"{first} {last}"
print(full_name)
print(research_name.find("Pat"))
print(research_name.replace("a", "o"))
print("lysis" in research_name)
print("patient" not in research_name)

#simple (x,y) inout and output as temperature 
x = input("x: "" ")
y = int(x) + 2
print(f"x: {x} , y: {y}")

temperature = input("temperature;  ") #conditional statement
temperature = int(temperature)
if 18 < temperature <= 35:
    print("Warm weather, fit for picnic")
elif 0 > temperature <= 18:
    print("Too cold, stay inside")
else:
    print("Undefined and not recommended to go outside")
print ("Have a great day")

#Notes app based on keywords, automatic sorting and categorization of notes