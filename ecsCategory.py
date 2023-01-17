# python script that includes text categorization based on keyword categories


import csv
import requests
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Initialize the Google Cloud Natural Language client
client = language.LanguageServiceClient()

# Function to extract keywords, key phrases and classify text
def extract_classify_text(url, csv_file):
    # Make a GET request to the website
    response = requests.get(url)

    # Get the text from the website
    text = response.text

    # Create a document object with the text
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT
    )

    # Use the client to analyze the text
    entities = client.analyze_entities(document).entities
    phrases = client.analyze_syntax(document).tokens
    classify_text = client.classify_text(document).categories

    # Create a dictionary to store the keywords and their salience scores
    keywords = {}
    keyphrases = {}
    classifications = {}

    # Iterate through the entities and add them to the dictionary
    for entity in entities:
        if entity.salience > 0:
            keywords[entity.name] = entity.salience

    # Iterate through the phrases and add them to the dictionary
    for phrase in phrases:
        if phrase.part_of_speech.tag == enums.PartOfSpeech.Tag.NOUN_PHRASE:
            keyphrases[phrase.text.content] = phrase.part_of_speech.confidence

    # Iterate through the classify_text and add them to the dictionary
    for classification in classify_text:
        classifications[classification.name] = classification.confidence

    # Sort the keywords by salience in descending order
       sorted_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)
    sorted_keyphrases = sorted(keyphrases.items(), key=lambda x: x[1], reverse=True)

    # read the csv file and match the classifications with predefined words
    with open(csv_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            for key, value in classifications.items():
                if key.split("/")[-1] in row.values():
                    classifications[key] = row["name"]
    return sorted_keywords, sorted_keyphrases, classifications

# Extract keywords, keyphrases and classify text from a website
url = 'https://www.example.com/posts'
csv_file = 'classification.csv'
keywords, keyphrases, classifications = extract_classify_text(url, csv_file)
print(keywords)
print(keyphrases)
print(classifications)


#Note: In this script, I added a new function called extract_classify_text which takes two arguments url and csv_file. The csv file should have a predefined list of words that you want to classify your text against. The csv should have two columns "name" and "classification" where name is the predefined words and classification is the category you want to classify your text against. The script reads the csv file and matches the classification of the text with the predefined words. If a match is found, the script replaces the classification name with the predefined name.

