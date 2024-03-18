# 3005-ASSINGMENT3

firstoly you should have psostges working if not go to the classs bright space instructions are there on how to do it
after that you would need to link  pyhton to the postgres 
in the terminal type "pip install psycopg2"
after this you should be able to link your python files to the table
at the begining of the file type the following 
right click on the database you'll be working on
click properties
get the database information as it would be needed in future steps
import psycopg2
conn = psycopg2.connect(host = "hostname", dbname="databasename", user="username", password ="password (postgres by default", port = port number )

after following the instructions above you shuold be able to run the code in your terminal .

Video LInk: https://youtu.be/SazHcXuAGAU
