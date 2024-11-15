# Function to calculate BMI
def calculate_BMI(Weight, Height):
    Height = Height/100
    BMI = Weight/(Height**2)
    return BMI

# Function to recommendation BMI
def recommendation_BMI(BMI):
    if (11 < BMI < 47) :
        if (BMI<=16) :
            return "You are very skinny. Manage your food intake!"
        elif (BMI<=18.5) :
            return "You are skinny to manage your intake!"
        elif (BMI<=25) :
            return "You are in the ideal posture. Preserve!"
        elif (BMI<=30) :
            return "You're overweight. Regulate your diet!"
        else :
            return "You are very overweight. Diet soon!"
    else :
        return "The number you entered is wrong"

# Input from the user
Height = float(input("Height (cm)? "))
Weight = float(input("Weight (kg)? "))

# Calculate BMI
BMI = calculate_BMI(Weight, Height)

# Classify BMI
recommendation = recommendation_BMI(BMI)

# Display the result
print("Body Mass Index: ",BMI)
print("Recommendations for you: ",recommendation)