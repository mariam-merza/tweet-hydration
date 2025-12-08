# tweet-hydration
An implementation of tweet hydration using the ANTiVax dataset: https://github.com/sakibsh/ANTiVax
## ANTiVax Dataset Hydration Process
Notes:
- Make sure you add your bearer token from the X developer portal in the empty quotation marks within the client part of the code (I recommend saving your bearer token into a .txt file since you cannot view it again without regenerating a new key).
- Not all tweets from the dataset can be hydrated due to deletion or being made private. 

## Steps: 
1. Download all csv files under the VaccineTweets folder in the GitHub repository: https://github.com/sakibsh/ANTiVax. Store them all within a single folder named “csv_files.” 
2. Use the built-in Windows command prompt and navigate to the folder where your CSV files are stored:
cd C:\Users\admin\Documents\csv_files 
Then use the following prompt to combine them: 
copy *.csv all-csv-files.csv 
3. Download the tweepy library in python: https://docs.tweepy.org/en/stable/install.html 
** Make sure it is saved in the same environment as the file you use to hydrate.
4. tweet-hydration.py includes the coding process for hydrating [20] tweets and output is stored into misinfo_hydrated.jsonl.
