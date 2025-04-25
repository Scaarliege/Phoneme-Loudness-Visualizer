import requests

phoneme_loudness = {
    'i': 4, 'ɪ': 4, 'e': 4, 'ɛ': 4, 'æ': 5, 'a': 5, 'ɑ': 5, 'ʌ': 4, 'ə': 4, 'ɜ': 4, 'o': 4, 'ɔ': 4, 'u': 4, 'ʊ': 4,
    'aɪ': 4, 'eɪ': 4, 'ɔɪ': 4, 'aʊ': 4, 'oʊ': 4, 'ɪə': 4, 'eə': 4, 'ʊə': 4,
    'v': 3, 'ð': 3, 'z': 3, 'ʒ': 3, 'f': 3, 'θ': 3, 's': 3, 'ʃ': 3, 'h': 3, 'l': 3, 'r': 3, 'ɹ': 3, 'w': 1, 'j': 1,
    'b': 2, 'd': 2, 'g': 2, 'p': 2, 't': 2, 'k': 2, 'm': 2, 'n': 2, 'ŋ': 2,
    'tʃ': 3, 'dʒ': 3,
    'ː': 0, 'ˑ': 0, '̃': 0, 'ˈ': 0, 'ˌ': 0, '̩': 0, '̯': 0, '˞': 0, '̥': 0, '̬': 0, '̤': 0, '̰': 0, '̻': 0, '̺': 0,
}

unknown_phoneme_loudness = 2
known_phonemes = sorted(phoneme_loudness.keys(), key=lambda x: -len(x))

def get_phonetic(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, f"Error: Unable to find the word '{word}'."
    try:
        data = response.json()
        phonetics = data[0].get("phonetics", [])
        for p in phonetics:
            if 'text' in p and p['text']:
                return p['text'], None
        return None, "Phonetic transcription not available."
    except Exception as e:
        return None, f"Error parsing phonetic data: {e}"

def extract_phonemes(phonetic_str):
    cleaned = phonetic_str.strip("/[] ").replace("ˈ", "").replace("ˌ", "")
    phonemes = []
    i = 0
    while i < len(cleaned):
        match = None
        for p in known_phonemes:
            if cleaned[i:i+len(p)] == p:
                match = p
                break
        if match:
            phonemes.append(match)
            i += len(match)
        else:
            if cleaned[i] not in [' ', '.', "'", "ː", "ˑ", "̃"]:
                print(f"Unrecognized phoneme or symbol: '{cleaned[i]}'")
                phonemes.append(cleaned[i])
            i += 1
    return phonemes

def get_loudness_data(phonemes):
    x, y = [], []
    for symbol in phonemes:
        x.append(symbol)
        y.append(phoneme_loudness.get(symbol, unknown_phoneme_loudness))
    return x, y