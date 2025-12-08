import tweepy
import csv
import json

tweet_ids = []
with open("all-csv-files.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        val = row["id"].strip()
        if val.lower() != "id" and val.isdigit():
            tweet_ids.append(int(val))

test_ids = tweet_ids[:20]

client = tweepy.Client(
    bearer_token=" "
)

response = client.get_tweets(
    ids=test_ids,
    tweet_fields=["id", "created_at", "text"]
)

output_file = "misinfo_hydrated.jsonl"

if response.data:
    with open(output_file, "w", encoding="utf-8") as out_file:
        for tweet in response.data:
            print(f"ID: {tweet.id}\nCreated at: {tweet.created_at}\nText: {tweet.text}\n")
            json.dump({
                "id": tweet.id,
                "created_at": str(tweet.created_at),
                "text": tweet.text
            }, out_file)
            out_file.write("\n")

    print(f"Hydrated {len(response.data)} out of {len(test_ids)} tweets.")
    print(f"Saved to {output_file}")
else:
    print("No tweets returned (deleted or private).")