import psycopg2
from django.http import Http404


#save changes on database
'''receives in three parameters:
    1. primary key for the database: in our case it's email
    2. field to be updated i.e name of the column
    3. the updates: information to save
    
    Note all parameters are string values'''
def edit(request_key, request_field, request_update):
    #establish connection to the database
    try:
        conn = psycopg2.connect(

                    host = "",     #host name of the server
                    database = "", #database name that you want to querry from
                    port = "",     #port number 
                    user = "",     #username to access databae
                    password = ""  #password for the database
        )
    except:
        raise HTTp404("incorrect request") 
        #raising this because my api is called from a web client
        #if you're not using Http request, you can print the error

    try:
        #generate cursor
        cur = conn.cursor()

        # we are updating the request_field of the row whose email matches the request_key
        #Note: replace {table_name} with valid table name from the database
        sql = "UPDATE {table_name} SET " + request_field + "= %s" + "WHERE email = %s"
        cur.execute(sql, (request_update, request_key))

        #commit the changes
        conn.commit()

        #close cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    #close the connection
    conn.close()