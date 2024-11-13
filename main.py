import spacy
nlp = spacy.load("en_core_web_sm")

keywords_to_attributes = {
    "sad": {"mood": "sad", "energy": "low", "genre" : "ballad"},
    "happy": {"mood": "happy", "energy": "high", "genre" : "pop"},
    "chill": {"mood": "chill", "energy": "medium", "genre" : "indie/alternative"},
    "romantic": {"mood": "romantic", "energy": "low/medium", "genre" : "R&B/soul"},
    "angry": {"mood": "angry", "energy": "high", "genre" : "rock"},
}

def get_playlist_attributes(title):
    doc = nlp(title.lower())
    attributes = {
        "mood": None,
        "energy": None,
        "genre": None
    }
    
    
    for token in doc:
        keyword = token.text
        if keyword in keywords_to_attributes:
            for key, value in keywords_to_attributes[keyword].items():
                attributes[key] = value
    
    return attributes

def generate_playlist(attributes):
    # Assuming you’re using the Spotify API, pseudocode for a query:
    search_query = f"{attributes['mood']} {attributes['energy']} {attributes['genre']}"
    # Call to API here with `search_query` as search input
    # Parse API response to build playlist
    playlist = ["Song1", "Song2", "Song3"]
    return playlist


title = "sad girl autumn"
attributes = get_playlist_attributes(title)
playlist = generate_playlist(attributes)
print("Generated playlist based on attributes:", playlist)



