import Levenshtein
from src.utils import config_manager

config = config_manager.load_config("config.json")
bad_words = config.get("bad_words", [])


def is_bad_word(word, threshold=90):
    for bad_word in bad_words:
        if Levenshtein.ratio(word.lower(), bad_word) * 100 >= threshold:
            return True
    return False
