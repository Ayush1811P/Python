# ✅ UNIT 4 - Complete Setup Verification

print("--- Checking all Unit 4 modules ---\n")

# CGI & Web
try:
    import cgi
    import http.cookies
    import requests
    print("✅ CGI & Web modules OK!")
except Exception as e:
    print(f"❌ CGI/Web Error: {e}")

# Database
try:
    import mysql.connector
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="88008191"  # 🔴 Replace this
    )
    if conn.is_connected():
        print("✅ MySQL Database connected OK!")
        conn.close()
except Exception as e:
    print(f"❌ MySQL Error: {e}")

# Time modules
try:
    import time, sched, calendar
    from dateutil import parser
    print("✅ Time modules OK!")
except Exception as e:
    print(f"❌ Time Error: {e}")

# Execution Control
try:
    import gc
    exec("x = 1 + 1")
    print("✅ Execution Control OK!")
except Exception as e:
    print(f"❌ Execution Error: {e}")

# Threads
try:
    import threading, queue
    print("✅ Threading modules OK!")
except Exception as e:
    print(f"❌ Threading Error: {e}")

print("\n--- All checks complete! Ready for Unit 4 🚀 ---")
