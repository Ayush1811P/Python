file = open("client_employee_data_2025.csv","r")
lines=file.readlines()
header=lines[0]
employees=lines[1:]
data=employees[0].strip().split(",")
emp_id=data[0]
name=data[1]
email=data[2]
age=data[3]
department=data[4]
designation=data[5]
salary=data[6]
working_hours=data[7]
leaves=data[8]
appraisal=data[9]
appraisal_amount=data[10]
performance_score=data[11]
status=data[12]
print("Employee Name: ",name)
print("Department: ",department)
print("Salary: ",salary)
print("Performance_Score: ",performance_score)
print("Status: ",status)

file.close()