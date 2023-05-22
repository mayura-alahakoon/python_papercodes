def calDiscount(consultationFee, typeofConsultation):
    


patientName = str(input("Enter the patient name: "))
typeofConsultation = str(input("Enter the type of consultation: 1. General 2. Special: "))
if typeofConsultation == "1":
    typeofConsultation = "General"
elif typeofConsultation == "2":
    typeofConsultation = "Special"
else:
    print("Invalid type of consultation")
    exit()

consultationFee = int(input("Enter the consultation fee: "))
discount = calDiscount(consultationFee, typeofConsultation);

