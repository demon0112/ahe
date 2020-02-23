Flask has been used for the api development:
Installation instructions:
PLease run the following command to install the required packages:
* pip install flask
* pip install pandas
* pip install matplotlib
* pip install ------------(any package which cannot be imported while executing the python files)

Database has been built using postgre:
In this case :
database = "ahe", user = "postgres", password = "demon0112"
please install postgres and give provide username and password during installation
two table have been created:
1.SOLARPOWER
2.LOADPOWER
Please execute importdb.py tp create tables after creating the db.
**pip install pyscopg2 
THIS IS TO CONNECT DATABASE THROUGH PYTHON 
  
 To fetch data minute-wise and hourly average execute fetch_data.py:
 The server is running at local host.
 For 
 1.min-wise solar data go to the url:localhost:portnumber/minute_solar_power
 2.min-wise load data go to the url:localhost:portnumber/minute_load_power
 3.hour-wise solar data go to the url:localhost:portnumber/hourly_solar_power
 4.hour-wise load data go to the url:localhost:portnumber/hourly_load_power
 
 For graphs execute file graph.py:
 The server is running at local host.
 For 
 1.min-wise graph go to the url:localhost:portnumber/plot_min.png
 2.hour-wise graph go to the url:localhost:portnumber/plot_hour.png
 
 Screenshots are attached for references
