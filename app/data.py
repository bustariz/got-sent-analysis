from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from statistics import mean
import nltk
from pymongo import MongoClient


def run_functions():
    dictionary = got_sent_analysis()

    import_to_mongo(dictionary)


# function to create df from csv and add needed columns to script csv and exports to dictionary
# path = 'Game_of_Thrones_Script.csv'
def got_sent_analysis():

    path = '../Game_of_Thrones_Script.csv'

    script_df = pd.read_csv(path)

    script_df = script_df.rename(columns = {'Release Date': 'release_date',
                                            'Season': 'season',
                                            'Episode':'episode',
                                            'Episode Title':'episode_title',
                                            'Name':'name', 
                                            'Sentence': 'sentence'
                                        })


    # sentiment analysis for script df using vaderSentiment library
    analyzer = SentimentIntensityAnalyzer()
    sent_analysis = [analyzer.polarity_scores(sentence) for sentence in script_df.sentence]

    # adds column to df for each polarity score (pos,compound,neu,neg)
    script_df['positive_score'] = [key.get('pos') for key in sent_analysis]
    script_df['compound_score'] = [key.get('compound') for key in sent_analysis]
    script_df['neutral_score'] = [key.get('neu') for key in sent_analysis]
    script_df['negative_score'] = [key.get('neg') for key in sent_analysis]

    # using nltk to separate sentence into words and punctuation as a list and add as a column into df
    script_df['tokenized_words'] = [nltk.word_tokenize(sentence)for sentence in script_df.sentence]


    # tokenized_words column with punctuation removed 
    script_df['alphanumeric_words'] = script_df.tokenized_words.apply(lambda x: [item for item in x if item.isalnum()])


    #adds column for word count within stripped down sentences
    script_df['word_count'] = [len(words) for words in script_df.alphanumeric_words ]
    script_df


    # converts df into dictionary and adds to mongodb
    script_dict = script_df.to_dict('records')
    
    
    
    return script_dict



def import_to_mongo(dictionary):
    client = MongoClient('mongodb://localhost:27017/')

    # setting variable for db
    db = client.sent_analysisdb

    # setting variable for collection in db
    col = db.got_scripts

    col.remove({})
    # inserts dictionary into db
    col.insert_many(dictionary)

    client.close()








