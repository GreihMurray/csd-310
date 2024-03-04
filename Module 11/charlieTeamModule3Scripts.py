import mysql.connector

# Database connection parameters
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor",
  database="wilsonfinancial"
)

# create a cursor object
crsr = db.cursor()


# report for clients that joined in the last 6 months
report1 = ("""
SELECT CURDATE() AS report_date, clientid, name FROM clients WHERE joined_date >= DATE_SUB(now(), INTERVAL 6 MONTH);
""")

# run the report command and prints the results
crsr.execute(report1)
report1Result = crsr.fetchall()
print("Report 1 result:")
for row in report1Result:
    print("Report Date: {}\nClient Id: {}\nClient Name: {}\n".format(row[0], row[1], row[2]))


# report for average price from the assets
report2 = ("""
SELECT CURDATE() AS run_date, AVG(price) AS avg_price FROM clientassets;
""")

# run the report command and prints the results
crsr.execute(report2)
report2Result = crsr.fetchall()
print("\nReport 2 result:")
for row in report2Result:
    print("Report Date: {}\nAvg Asset Price: {}\n".format(row[0], row[1]))


# report for up to 10 transactions made per client over the last month
report3 = ("""
SELECT CURDATE() AS report_date, tr.clientid, cl.name, COUNT(*) AS monthly_transactions FROM clienttransactions AS tr JOIN clients AS cl ON cl.clientid = tr.clientid WHERE transaction_date >= DATE_SUB(now(), INTERVAL 1 MONTH) GROUP BY clientid HAVING COUNT(*) > 10;
""")

# run the report command and prints the results
crsr.execute(report3)
report3Result = crsr.fetchall()
print("\nReport 3 result:")
for row in report3Result:
    print("Report Date: {}\nClient Id: {}\nClient Name: {}\nMonthly Transactions: {}\n".format(
        row[0],
        row[1],
        row[2],
        row[3]))
