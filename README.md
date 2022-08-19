<br/>
<p align="center">
  <h1 align="center">IT Test</h1>

  <p align="center">
    Practical test in python
    <br/>
    <br/>
  </p>
</p>



## About The Project

1. Check the exchange rate from Euros to Dollars on 5 different days from the following page https://finance.yahoo.com/currency-converter:
2. Store the exchange value data in a SQL database.
3. Develop a REST API prototype that allows querying the exchange value stored in the SQL database.
4. At the end of the process hit the webhook at URL: https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9 with a body that includes the exchange value queried


## Built With

* Python 3.7.9
* PostgreSQL 13



## Getting Started


### Prerequisites

You need to use python 3.7.9 and install this dependencies

* yahoofinancials==1.6
* requests==2.28.1
* psycopg2==2.9.3
* Flask==2.2.2


### Installation

####1. Clone the repo
* git clone https://github.com/AdrianAlejandro94/IT_test.git

####2. Install Python 3.7.x

####3. install Requirements
* pip install -r requirements.txt

####4. Create Database in PostgreSQL
CREATE TABLE public.prices (
	"date" int4 NULL,
	high float4 NULL,
	low float4 NULL,
	"open" float4 NULL,
	"close" float4 NULL,
	volume int4 NULL,
	adjclose float8 NULL,
	formatted_date date NULL
);
CREATE UNIQUE INDEX prices_formatted_date_idx ON public.prices USING btree (formatted_date);


####5. In database.py change the configuration of PostgreSQL 

      on = psycopg2.connect(user="postgres",
                           password="postgres",
                           host="127.0.0.1",
                           port="5432",
                           database="IT_testing")


####6. Start the main.py File


### USAGE

When the main.py is executed is going to obtain the data from finance yahoo
and store the exchanges of the selected dates on yahoofinantials.py in the database.

Then the server with flask is going to start on localhost in the port 5000

When you make a get to this direction is going to get the exchanges of the date selected
Example: http://localhost:5000/exchange?date=2022-08-04

Then is going to make a post request to the weebhook URL with the exchange data in the body