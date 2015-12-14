import tweepy

consumer_key = "gUmh2dbIUNR9mvy4RUHe4OK4I";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "kCEJ3Y7orsz0VU5m7xLlpFZXGeJF5GVfcDGqRVXX9pYFDsgV1d";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "99208580-yDlnmwSdTbIt0Mp9JJT4EsDTRUMYIhLBHAmM7T8OG";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "vmBe7Atg910MII7tDfqmnERFeooGPPBUGciBZkzhpOGBJ";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



