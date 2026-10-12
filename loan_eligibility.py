customer_id = input("Enter Customer ID: ")
income = float(input("Enter Monthly Income (₹): "))
loan_amount = float(input("Enter Requested Loan Amount (₹): "))
emi = float(input("Enter Existing Monthly EMI (₹): "))
employment = input("Enter Employment Type (Salaried/Self-employed): ").strip().lower()
credit_score = int(input("Enter Credit Score: "))

emi_limit = income * 0.50

if employment == "salaried" and credit_score >= 750 and income >= 30000:
    if emi <= emi_limit:
        eligibility = "Eligible for Pre-Screening"
        category = "Standard"
        remarks = "Meets standard preliminary criteria"
    else:
        eligibility = "Not Eligible"
        category = "None"
        remarks = "Existing EMI exceeds permissible limit"

elif 650 <= credit_score <= 749:
    if emi <= emi_limit:
        eligibility = "Eligible for Pre-Screening"
        category = "Restricted"
        remarks = "Subject to additional verification"
    else:
        eligibility = "Not Eligible"
        category = "None"
        remarks = "Existing EMI exceeds permissible limit"

else:
    eligibility = "Not Eligible"
    category = "None"
    remarks = "Minimum eligibility requirements not met"

print("\n===== LOAN ELIGIBILITY PRE-SCREENING =====")
print("Customer ID       :", customer_id)
print("Employment Type   :", employment.title())
print("Monthly Income    : ₹", income)
print("Credit Score      :", credit_score)
print("Existing EMI      : ₹", emi)
print("Requested Amount  : ₹", loan_amount)
print("Loan Eligibility  :", eligibility)
print("Eligibility Category:", category)
print("Remarks           :", remarks)
print("\nNote: This is a preliminary assessment, not loan approval.")