#!/usr/bin/python

import sys
import psycopg2

def query_db(argv):
    # connect to postgres database Tcount using psycopg2
    conn = psycopg2.connect(database="Tcount", user="NOSUPERUSER", password="otherpassword", host="localhost", port="5432")
    # create cursor
    cur = conn.cursor()
    # execute select statement to extract words and counts from Tweetwordcount table
    sql_query = "SELECT word, count from Tweetwordcount where (count>=" + str(sys.argv) + " and count<=" + str(sys.argv) + ");"
    cur.execute(sql_query)
    # fetch all records from select statement
    records = cur.fetchall()
    # loop through records and print results
    for rec in records:
        print "word = ", rec[0]
        print "count = ", rec[1], "\n"
    conn.commit()
    # close connection
    conn.close()

if __name__ == "main":
    query_db(argv)
