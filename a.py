#import psycopg2
#try:
#    conn = psycopg2.connect(
#        host="localhost",
#        database="sab",
#        user="sabuser",
#        password="sab@5432"
#    )
#    print("Connection successful!")
#    conn.close()
#except psycopg2.OperationalError as e:
#    print(f"Connection failed: {e}")

import psycopg2

def run_query(query):
    conn = None
    try:
        # 1. Establish a connection
        conn = psycopg2.connect(
            host="localhost",
            database="sab",
            user="sabuser",
            password="sab@5432",
            port=5432 # Default PostgreSQL port
        )

        # 2. Create a cursor object
        cur = conn.cursor()

        # 3. Execute the SQL query
        cur.execute(query)

        # 4. Fetch the results
        # Use fetchone(), fetchall(), or fetchmany()
        records = cur.fetchall()

        # 5. Process the results (optional)
        for row in records:
            print(row)

        # 6. Close the cursor and connection
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

# Example usage
sql_query = "SELECT * FROM api_phdcppc;"
run_query(sql_query)
