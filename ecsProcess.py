def extract_classify_sentiment(url):
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
    sentiment = client.analyze_sentiment(document).document_sentiment

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
        subcategory = classification.name.split("/")[-1]
        classifications[subcategory] = classification.confidence

    # Sort the keywords by salience in descending order
    sorted_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)
    sorted_keyphrases = sorted(keyphrases.items(), key=lambda x: x[1], reverse=True)

    return sorted_keywords, sorted_keyphrases, classifications, sentiment.score
