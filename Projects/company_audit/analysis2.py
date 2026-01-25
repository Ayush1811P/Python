file=open("client_employee_data_2025.csv","r")
lines=file.readlines()
employees=lines[1:]

    #COUNTING TOTAL EMPLOYEES
count=0
for emp in employees:
    count +=1

    #EVALUATION OF TOTAL SALARIES PER MONTH
Total_salaries=0
for emp in employees:
    data=emp.strip().split(",")
    salary=int(data[6])
    Total_salaries=Total_salaries+salary
    #print(salary)

print("Total salary: ",Total_salaries)



        #TOTAL EMPLOYEES ON BENCH 
        #WHO ARE TAKING SALARIES
bench_employees=0
for emp in employees:
    data=emp.strip().split(",")
    status=data[12]

    if status=="Bench":
        bench_employees+=1

#print("Total employees on bench: ",bench_employees)   
# active_employees=[]
# for emp in employees:
#     data=emp.strip().split(",")
#     status=data[12]  
#     if status!="Bench":
#         active_employees.append(emp)


#print(active_employees)

bench_salary=0
for emp in employees:
    data=emp.strip().split(",")
    status = data[12]
    salary=int(data[6])

    if status=="Bench":
        bench_salary += salary

print("total money spent on benched employees: ",bench_salary)
active_employees_salary=Total_salaries-bench_salary
print("only active employees salary: ",active_employees_salary)
file.close()    
