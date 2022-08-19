import psycopg2


def get_connection():
    """
        Method for connect to Database with PostgreSQL Credentials
    :return:
    """
    con = psycopg2.connect(user="odoo",
                           password="Citytech.2k20!",
                           host="127.0.0.1",
                           port="5432",
                           database="IT_testing")  #connection
    cur = con.cursor()  #cursor
    return con, cur


def store_database(data):
    """
        Method for store data from yahoo exchanges in the database
    :param data:
    :return:
    """
    try:
        con, cur = get_connection()  # connection to database

        for query in data['EURUSD=X']['prices']:
            data = "INSERT INTO public.prices(date, high, low, open, close, volume, adjclose, formatted_date) VALUES (%s, %s, %s, %s, %s, %s, %s, '%s')" % \
                   (query['date'], query['high'], query['low'], query['open'], query['close'], int(query['volume']), query['adjclose'], query['formatted_date'])  # Insert Exchanges to database

            data += "ON CONFLICT(formatted_date) DO UPDATE SET date = %s, high = %s, low = %s, open = %s, close = %s, volume = %s, adjclose = %s, formatted_date = '%s'"% (
                int(query['date']), query['high'], query['low'], query['open'], query['close'], int(query['volume']), # If exists record UPDATE
                query['adjclose'], query['formatted_date'])

            cur.execute(data)  # execute query
            con.commit()  # confirm changes in database

    except (Exception, psycopg2.Error) as error:  # if error display on console
        print("Failed to insert record into prices table", error)

    finally:
        if con:  # if connection succesfully
            cur.close()  # close cursor
            con.close() # close connection
            print("PostgreSQL connection is closed")


def exchange(date):
    """
        Method for obtain data from the database by Date
    :param date:
    :return:
    """
    try:
        con, cur = get_connection() # connection to database
        cur.execute("""select row_to_json(PRICES) from (SELECT * FROM prices WHERE formatted_date = %s) PRICES""",
                    [date])  # query for obtain prices and values in Json format
        result = cur.fetchone()  # method returns a single record or None if no more rows are available
    except (Exception, psycopg2.Error) as error:  # if error display on console
        print("Failed to fetch record into prices table", error)
    finally:
        if con:  # if connection succesfully
            cur.close()  # close cursor
            con.close()  # close connection
            print("PostgreSQL connection is closed")
    return result
