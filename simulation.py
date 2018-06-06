from bank import create,sum_balance,memory_clear
from random import normalvariate
student_trial=[]
senior_trial=[]
marketing_spend=25000
trials=1000
firstname='leo'
lastname='singh'
for trial in range(trials):

    number_account_student=int(normalvariate(100000,15000))
    number_account_senior=int(normalvariate(60000,7500))
    for i in range(number_account_student):
        balance_student = normalvariate(3000,750)
        create(firstname,lastname,balance_student)

    total_student=sum_balance()
    student_trial.append(total_student)
    memory_clear()


    for i in range(number_account_senior):
        balance_senior = normalvariate(10000,2500)
        create(firstname,lastname,balance_senior)

    total_senior=sum_balance()
    senior_trial.append(total_senior)
    memory_clear()

total_college_trials=sum(student_trial)
total_senior_trials=sum(senior_trial)
expected_amount_student=total_college_trials/len(student_trial)
expected_amount_senior=total_senior_trials/len(senior_trial)
roi_student = (expected_amount_student*0.10) - marketing_spend
roi_senior = (expected_amount_senior*0.10) - marketing_spend
print("Expected Total Deposit: -")
print("College student plan: ${0:,.2f}\nSenior citizen plan: ${1:,.2f}".format(total_college_trials,total_senior_trials))
print("\n")
print("Expected Return on Investment: -")
print("College student plan: ${0:,.2f}\nSenior citizen plan: ${1:,.2f}".format(roi_student,roi_senior))
