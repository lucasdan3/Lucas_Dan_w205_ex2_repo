This Readme.txt file shows step-by-step instructions on how to run the Twitter Application for my W205 Exercise 2:

1) Launch an ec2 instance using an AMI that contains all of the necessary programs as instructed in the directions

2) If the AMI does not contain the necessary installations, you must install the following programs:

	a) PostgreSQL
	b) python2.7.10
	c) python library psycopg2 for interacting with PostgreSQL via python
	d) python library tweepy for interacting with Twitter API via python
	e) Apache Storm
	f) lein
	g) python library streamparse for streaming data via python
	h) python library virtualenv

3) Note that you must change all of the necessary permissions for the installations above, as instructed in the assignment

4) Make sure you navigate to the directory /home/ec2-user/EX2Tweetwordcount/ex2

5) Once the environment is set up and you have navigated to the ex2 directory, we are ready to run the Twitter Application. However, the only way I was able to get this to work was by manually configuring PostgreSQL first. I'm not sure if this could cause any problems, but it's possible. However, I did my absolute best to configure all of the scripts such that they would run smoothly with my PostgreSQL configuration.

6) To test the streaming application run the command python hello-stream-twitter.py and watch the tweets stream!

7) Now we will use streamparse, so run the command sparse run -d. This will stream in tweets, parse the tweets by extracting words, count all words, connect to a Postgres database instance, and create the Tcount database/Tweetwordcount table if everything is properly configured (configuration took me so long).

8) For the serving scripts, run the command python finalresults.py and pass in as many arguments as you'd like. This script will connect to our Tcount database, select the word count corresponding to the arguments passed in, and output the results (i.e. word counts for each argument) as instructed.

9) Finally, run the command python histogram.py and pass in 2 arguments (i.e. integers k1 and k2). The script will output all words for which their total number of occurrences in the stream is greater than or equal to the first argument and less than or equal to the second argument, as instructed.