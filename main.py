import math as math

def ask():
    response  = input("""What do you want to calculate?\ntype "n" - for the number of months,\ntype "a" - for the monthly payment:\n type "p" for the credit principal""")

    if response == "n" :
        credit_principal = int(input("Enter the credit principal:"))
        annuity_payment = int(input("Enter the monthly payment:"))
        credit_interest = float(input("Enter the credit interest:"))/1200
        number_of_payments = math.ceil(math.log((annuity_payment / (annuity_payment - credit_interest * credit_principal)),(1 + credit_interest)))
        years_months = math.modf(number_of_payments/12)
        if years_months[1] != 0:
            print("You need ",math.ceil(years_months[1]),"years and ",round(years_months[0]*12), " months to repay the credit")
        else:
           print("You need ",math.ceil(years_months[0]*12), " months to repay the credit")
    elif response == "a":
        credit_principal = int(input("Enter the credit principal:"))
        months = int(input("Enter the number of periods:"))
        credit_interest = float(input("Enter the credit interest:"))/1200
        annuity_payment = credit_principal * (credit_interest * math.pow(1 + credit_interest, months)) / (math.pow(1 + credit_interest, months) - 1)
        print("Your annuity payment =",math.ceil(annuity_payment),"!")
    elif response == "p":
        annuity_payment = float(input("Enter the annuity payment:"))
        months = int(input("Enter the number of periods:"))
        credit_interest = float(input("Enter the credit interest:"))/1200
        credit_principal = annuity_payment / ((credit_interest * math.pow(1 + credit_interest, months)) / (math.pow(1 + credit_interest, months) - 1))
        print("Your credit principal = ",credit_principal)
ask()



