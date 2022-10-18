####Initial variables
accountNo = None
month = str
months = ["1","2","3","4","5","6","7","8","9","10","11","12"]

ePlan = str
ePlanChoice= ["EFIR","EFLR"]
eUsage = None
eleRateU1000 = 0.0836
eleRateA1000 = 0.0941
elerateFlt = 0.0911

gPlan = str
gPlanChoice= ["GFIR","GFLR"]
gUsage = None
gasrateU950 = 0.0456 
gasRateA950 = 0.0589 
gasRateFlt = 0.0393 

g_fixedMthFee = float
fixedMthFee = 120.62

taxrateA = 0.05
taxrateB = 0.13
taxrateC = 0.15
####Start
print("Welcome to the Global Energy bill calculator!")

#### input and validation
while accountNo == None:
     accountvalidate = input("Enter your account number.\n")
     if accountvalidate.isdigit():
        accountNo = int(accountvalidate)
     else:
        print("Invalid account number")

month = input("Enter the month number (e.g., for January, enter 1).\n")            
while month not in months:
    print('Please enter 1-12.')
    month = input("Enter the month number (e.g., for January, enter 1).\n")

ePlan = input("Enter your electricity plan (EFIR or EFLR).\n").upper()
while ePlan not in ePlanChoice:
    print(f'Please enter only {ePlanChoice[0]} or {ePlanChoice[1]}.')
    ePlan = input("Enter your electricity plan (EFIR or EFLR).\n").upper()

while eUsage == None:
    eleusedvalidate = input("Enter the amount of electricity you used in month "+str(month)+" (in kWh).\n")
    if eleusedvalidate.isdigit():
        eUsage = float(eleusedvalidate)
    else:
        print("Invalid input.")

gPlan = input("Enter your gas plan (GFIR or GFLR).\n").upper()
while gPlan not in gPlanChoice:
    gPlan = input("Enter your gas plan (GFIR or GFLR).\n").upper()
    print(f'Please enter only {gPlanChoice[0]} or {gPlanChoice[1]}.')

while gUsage == None:
    gUsagevalidate = input("Enter the amount of gas you used in month "+str(month)+" (in GJ).\n")
    if gUsagevalidate.isdigit():
        gUsage = float(gUsagevalidate)
    else:
        print("Invalid input.")

province =input("Enter the abbreviation for your province of residence (two letters).\n").upper()
while province not in ["AB","BC" , "MB" , "NT" , "NU" , "QC" , "SK" , "YT" , "ON" , "NB" , "NL" , "NS","PE"]:
    print('Please enter correct province.')
    province =input("Enter the abbreviation for your province of residence (two letters).\n").upper()

####Electric Fee
if ePlan == "EFIR":
    if eUsage <= 1000:
        eleFee = eUsage * eleRateU1000   
    else : eleFee = (eleRateU1000 * 1000) + ((eUsage -1000)*eleRateA1000)
else:
    eleFee = eUsage * elerateFlt 

####Gas Fee
if gPlan =="GFIR":
    if gUsage <= 950:
        gasFee = gUsage * gasrateU950
    else: gasFee = (gasrateU950 * 950) + (gasRateA950 * (gUsage - 950))
else:
    gasFee = gUsage * gasRateFlt

####Fixed monthly gas cost
if gUsage > 0:
   g_fixedMthFee = 1.32

####Tax rate
match province:
    case 'AB'|'BC'|'MB'|'NT'|'NU'|'QC'|'SK'|'YT':
        tax = taxrateA
    case 'ON':
        tax = taxrateB
    case 'NB'|'NL'|'NS'|'PE':
        tax = taxrateC


####Calculate total and print
billtotal = (eleFee + gasFee + fixedMthFee + g_fixedMthFee ) * (1 + tax)
print(f'Thank you! Your total amount due now is: ${billtotal:.2f}')