from entry_of_veicle import record
def Show_Data():
    if len(record)<1:
        print("Nothing To Show")
    for i in record:
        print(i)