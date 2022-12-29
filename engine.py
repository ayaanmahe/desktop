from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

# Pre-process the data
def preprocess_data(data):
    processed_data = []
    for doc in data:
        # Tokenize the text
        tokens = re.findall(r'\w+', doc['text'])
        # Stem the tokens
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        # Remove stop words
        filtered_tokens = [token for token in stemmed_tokens if token not in stop_words]
        processed_data.append({'google': doc['google'], 'tokens': filtered_tokens})
    return processed_data

