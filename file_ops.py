# Handles loading and saving data from JSON files.
# Used for both the vocabulary and the settings.


import json 
import os
VOCAB_FILE = "vocab.json"

#this functions loads the json file, checks if the file exists in order to the app not to crush in case there isn't needed file

def load_vocab():
    if not os.path.exists(VOCAB_FILE):
        print("No vocabulary file found. Starting with empty vocabulary.")
        return {}

    with open(VOCAB_FILE, "r", encoding="utf-8") as file: #encoding - to handle arabic and hebrew
        return json.load(file)

#this function saves or updates new dictionary (all unit, word and meaning) to the vocabulary
def save_vocab(unit: str, word: str, meaning: str) -> None:

    vocab = load_vocab()
    if unit not in vocab:
        vocab[unit] = []

    for entry in vocab[unit]:
        if entry["word"] == word:
            entry["meaning"] = meaning
            break
    else:
        vocab[unit].append({"word": word, "meaning": meaning})

    with open(VOCAB_FILE, "w", encoding="utf-8") as file:
        json.dump(vocab, file, indent=2, ensure_ascii=False)

#this function saves or updates new dictionary to the vocabulary
def save_vocab_file(data: dict) -> None:
    with open(VOCAB_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)