my_plants = ["spinach", "tomatoes", "mung beans", "peppers"]
moisture = [60, 50, 30, 25]  # Volumetric Water Content

irrigation_count = 0

# Ranges per plant
# Peppers - 23% to 27%
# Spinach - 41% to 80%
# Tomatoes- 40% to 80%
# Mung Beans - 16% to 35%

print(" Plants by Numbers: ")
print(" Spinach : 1")
print(" Tomatoes : 2")
print(" Mung Beans : 3")
print(" Peppers : 4")

def get_integer_input(prompt):
    while True:
        try:
            current_plant = input(prompt)
            return current_plant
        except ValueError:
            print("Invalid input! Please enter a whole number.")


plant_prompt = "Sensors currently analyzing plant number: "

plant = get_integer_input(plant_prompt)
num_plant = int(plant)

current_moisture = input("Sensors initially reading moisture: ")
num_moisture = int(current_moisture)

ideal_moisture = moisture[num_plant-1]

def irrigation_time (moist, ideal ):
    diff = ideal - moist
    time = diff/5
    full_time = int(time)

    return full_time



if num_plant==1:
    if num_moisture < 41:
        print("Irrigation System Activated for Spinach Section")
        fullTime = irrigation_time(num_moisture, ideal_moisture)
        print("Irrigation system was on for " + str(fullTime) + " minutes")
        print("New moisture is : " + str(ideal_moisture) + ", the ideal value!")


"""
    elif current_plant=="tomatoes":
        if current_moisture

    elif current_plant == "mung beans":
        if current_moisture

else:

"""
