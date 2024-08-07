import psycopg2
from psycopg2 import OperationalError

connection = None
try:
    connection = psycopg2.connect(database="fp_db", user='postgres', password='A1$habiya', host="localhost",
                                  port=5432)
    print("after conn")
    cursor = connection.cursor()
    print(cursor)

    sql_context = "SELECT * FROM public.emp_data"
    # sql_context = "INSERT into emp_data VALUES ('James', 2124, 'STE2' );"
    # sql_context = "DELETE from public.emp_data WHERE name='James';"
    # sql_context ="""
    # select
    #     *
    # from
    #     public.metrics sm
    # where
    #     sm.metric_name not like '%test%'
    # group by
    #     sm.metric_name
    # """

    cursor.execute(sql_context)
    # connection.commit()
    #
    # Fetch all rows from database
    record = cursor.fetchall()

    print("Data from Database:- ", record)
except OperationalError as e:
    print(f"The error '{e}' occurred")
# return connection
