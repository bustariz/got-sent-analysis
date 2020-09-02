import pandas as pd
# import numpy as np
from textblob import TextBlob
from sqlalchemy import create_engine
import psycopg2

# engine to connect to postgresql db
engine = create_engine('postgresql://postgres:bru1014ustz91@localhost/got_db')

# # Reads in script from csv file and renames columns to lowercase
path = '../data/Game_of_Thrones_Script.csv'

script_df = pd.read_csv(path)

script_df = script_df.rename(columns = {'Release Date': 'release_date',
                                        'Season': 'season',
                                        'Episode':'episode',
                                        'Episode Title':'episode_title',
                                        'Name':'name', 
                                        'Sentence': 'sentence'
                                       })

text_blobs = [TextBlob(sentence) for sentence in script_df.sentence]

script_df['tokenized_words'] = [sentence.words for sentence in text_blobs]
script_df['alpha_numeric_words'] = script_df.tokenized_words.apply(lambda x: [item for item in x if item.isalnum()])
script_df['word_count'] = [len(words) for words in script_df.alpha_numeric_words ]
script_df['polarity_score'] = [sentence.sentiment.polarity for sentence in text_blobs]
script_df['subjectivity_score'] = [sentence.sentiment.subjectivity for sentence in text_blobs]

script_df.to_sql('got_script',engine)
