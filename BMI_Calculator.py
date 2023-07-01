
try:
    Height = float(input("Please enter your height in metres: "))
    Weight = float(input("Please enter your weight in kg: "))

except:
    print("Invalid Input!")

BMI_Index= round(Weight / (Height * Height))
print("BMI for given height and weight is: ", BMI_Index)



if BMI_Index <16:
    print("Severely Underweight")
elif BMI_Index < 18.5:
    print("Underweight.")
elif BMI_Index <= 24.9:
    print("Normal.")
elif BMI_Index <= 29.9:
    print("Overweight.")
else:
    print("Obese.")