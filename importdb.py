import psycopg2

conn = psycopg2.connect(database = "ahe", user = "postgres", password = "demon0112", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE solarpower
      (TS TIMESTAMP PRIMARY KEY ,
      SOLARPOWER numeric(4,2) not null   );''')
print ("Table created successfully")
cur.execute('''COPY solarpower FROM 'C:\Users\Public\solar_power_data.csv' DELIMITER ',' CSV HEADER;''')

conn.commit()
conn.close()