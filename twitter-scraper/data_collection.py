"""
 * Data collection file, Created by Elias Vera-Jimenez
 * Last Updated: March 1st, 2023
"""

from twarc import Twarc2, expansions
import datetime
import locker # Key Locker for Tokens, not imported to github.
import time
import mongodb_connector


#base time for the program to run
timer_0 = time.time()

#initializing client w/ bearer token. 
client = Twarc2(bearer_token=locker.get_bearer_key())




def main():


    # Time where twarc will look for tweets
    start_time = datetime.datetime(2023, 2, 28, 0, 0, 0, 0, datetime.timezone.utc)

    # Time where twarc will stopp looking at tweets
    end_time = datetime.datetime(2023, 3, 1, 0, 0, 0, 0, datetime.timezone.utc)
    # Main query, keywords and such go here.
    query = open("query.txt", "r")

    #method calls the recent search endpoint to get tweets based on the query 
    search_results = client.search_recent(query=query.read(), start_time=start_time, end_time=end_time, max_results=100)

    # Returns all of the tweets found in the criteria above
    # and sends the data collected to the MongoDB collection for storage
    for page in search_results:
        result = expansions.flatten(page)
        for tweet in result:
            mongodb_connector.move_to_collection(tweet)

    query.close()

if __name__ == "__main__":
    print("Running Search ...")
    main()
    print("Complete. Time Elapsed: ", time.time() - timer_0)
