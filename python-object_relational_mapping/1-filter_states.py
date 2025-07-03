#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
It connects to a MySQL server running on localhost at port 3306.
The script takes three command-line arguments: MySQL username,
MySQL password, and the database name.
Results are sorted in ascending order by states.id.
"""
import MySQLdb
import sys


def filter_states_by_N(username, password, db_name):
    """
    Connects to the specified MySQL database and retrieves all records
    from the 'states' table whose 'name' starts with 'N' (case-sensitive).

    Args:
        username (str): The MySQL username to connect with.
        password (str): The MySQL password for the user.
        db_name (str): The name of the database to connect to.

    Returns:
        None: Prints the fetched states to standard output.
    """
    db_connection = None  # Initialize connection object to None
    try:
        # Establish a database connection to the MySQL server
        db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Create a cursor object using the connection
        cursor = db_connection.cursor()

        # Execute the SQL query to select states starting with 'N',
        # ordered by ID. The LIKE operator is used for pattern matching.
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' "
                       "ORDER BY id ASC")

        # Fetch all the rows returned by the executed query
        results = cursor.fetchall()

        # Print each row (tuple) retrieved from the database
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        # Catch and print any MySQL-specific errors that occur during
        # connection or query execution.
        print(f"Error connecting to the database or executing query: {e}")
        sys.exit(1)
    finally:
        # Ensure the database connection is closed if it was successfully
        # established, regardless of whether an error occurred or not.
        if db_connection:
            db_connection.close()


if __name__ == "__main__":
    # This block ensures the code runs only when the script is executed directly.

    # Check if the correct number of command-line arguments are provided.
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <mysql_username> <mysql_password> "
              "<database_name>")
        sys.exit(1)

    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the main function to filter and list states
    filter_states_by_N(mysql_username, mysql_password, database_name)
