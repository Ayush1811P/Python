import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="88008191",
    database="ipl"
)   
print("connected Successfully")
cursor=conn.cursor()

# table_name="clean_players"
# cursor.execute(f"SELECT * FROM {table_name}")
# for row in cursor:
#     print(row)

def is_valid_name(name):
    return name.isidentifier()
def create_table():
    table_name=input("Enter table name: ")
    if not is_valid_name(table_name):
        print(-1)
        return
    query=f"""
    CREATE TABLE IF NOT EXISTS {table_name}(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
    )
    """
    cursor.execute(query)
    print("Table created called {table_name}")

def display_data():
    table_name=input("Enter table name to display: ")
    cursor.execute(f"Select * from {table_name}")
    print(cursor)
    for row in cursor:
        print(row)

def insert_data():
    table_name=input("Enter table name: ")

    if not is_valid_name(table_name):
        print(-1)
        return
    cursor.execute(f"DESCRIBE {table_name}")
    columns=cursor.fetchall()

    col_names=[]
    values=[]
    print("\n\t Enter values")
    for col in columns:
        col_name=col[0]
        extra=col[5]

        if extra=="auto_increment":
            continue
        value=input(f"{col_name}: ")
        col_names.append(col_name)
        values.append(value)

    col_string=", ".join(col_names)
    placeholders=", ".join(["%s"]*len(values)) 
    query=f"INSERT INTO {table_name}({col_string}) VALUES ({placeholders})"  

    cursor.execute(query,values)
    conn.commit()
    print("Data inserted successfully!") 


def main():
    while True:
        print("1: create table\t2:Insert Values\t3: Display Data\t0:EXIT")
        choice=int(input("Ente choice: "))
        match choice:
            case 1:create_table()
            case 2:insert_data()
            case 3:display_data()
            case 0:return

        

main()  