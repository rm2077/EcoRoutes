# Calculate carbon emissions
def calculate_carbon_emissions():
    #initial values
    Distance_Traveling = float(input("Enter the total number of miles driving: "))
    Fuel_Usage = float(input("Enter the carbon content of the fuel in grams per gallon: "))
    Density = float(input("Enter the density of the fuel used: "))
    Heat_Values = float(input("Enter the heat value of the fuel used: "))
    
    # Calculate carbon emissions
    Travel_Carbon_Footprint = ((Distance_Traveling + Fuel_Usage) * 2.3 * Heat_Values * Density)

    # Print the result
    print(f"The estimated carbon emissions are {Travel_Carbon_Footprint:.2f} grams.")
# Call the function to calculate carbon emissions
calculate_carbon_emissions()