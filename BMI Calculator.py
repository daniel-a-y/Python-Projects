print("Welcome to the BMI Calculator ")
#input function
height= input("Please Enter your height in M (Metres):")
weight= input("Please Enter your weight in Kg (Kilograms):")
#change weight into integar and height into decimals (float)
bmi = int(weight) / float(height) ** 2
# shorten long bmi value by changing bmi into an integar
bmi_as_int= int(bmi)
print(bmi_as_int)
print("Thank you for using this BMI Calculator created by Daniel Adu-Yeboah")

