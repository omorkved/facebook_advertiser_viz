import spacy
import urllib3
import json
import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

http = urllib3.PoolManager()
nlp = spacy.load("en_core_web_sm")

parser = argparse.ArgumentParser()
parser.add_argument("--path", 
                    help="specify path to advertisers_who_uploaded_a_contact_list_with_your_information.json")

args = parser.parse_args()
if args.path:
    path_to_adv_file = args.path
    print("Using path: " + str(path_to_adv_file))
   
else:
    print("Using default path")
    path_to_adv_file = None


def load_file(advs_file = "advertisers_who_uploaded_a_contact_list_with_your_information.json"):
    with open(advs_file) as advs:
        data = json.loads(advs.read())

    advs_df = pd.DataFrame.from_dict(data)
    return advs_df

# Not invoked yet -- TODO switch on flag
def build_org_list(df):
    orgs = []
    for entry in df.itertuples():
        doc = nlp(entry[1])
        for ent in doc.ents:
            if ent.label_ == "ORG":
                print(ent.text)
                orgs.append(ent.text)
    return orgs


def wordcloud(fb_list, title):
    wordcloud = WordCloud(width=800, height=600).generate(fb_list)
    
    plt.figure(figsize=(15,10))
    # Display the generated image in a new window:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(title)
    plt.tight_layout(pad=4)
    plt.show()

if path_to_adv_file:
    advs_df = load_file(path_to_adv_file)
else:
    print("Using default path")
    advs_df = load_file()


wordcloud(" ".join(advs_df.custom_audiences.to_list()), title="Advertisers who have uploaded your Contact Info to Facebook include:")
