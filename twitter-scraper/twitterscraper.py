#importing the twarc and json libraries, for usage in this file.

from twarc import Twarc2, expansions
import datetime
import json
import locker # Key Locker for Tokens, not imported to github.


#initializing client w/ bearer token. 
client = Twarc2(bearer_token=locker.get_bearer_key())

def main():
    # Time where twarc will look for tweets
    start_time = datetime.datetime(2023, 2, 10, 0, 0, 0, 0, datetime.timezone.utc)

    # Time where twarc will stopp looking at tweets
    end_time = datetime.datetime(2023, 2, 14, 23, 0, 0, 0, datetime.timezone.utc)
    file_name = input("Where are we storing the data? ")
    # Main query, keywords and such go here.
    query = ""

    #method calls the recent search endpoint to get tweets based on the query 
    search_results = client.search_recent(query=query, start_time=start_time, end_time=end_time, max_results=100)

    #returns all of the tweets found in the criteria above
    for page in search_results:
        result = expansions.flatten(page)
        with open(file_name, 'w+') as filehandle:
            for tweet in result:
                filehandle.write(json.dumps(tweet) + "\n")
            

if __name__ == "__main__":
    main()

