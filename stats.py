def book_count_words(text):
    words = text.split()
    return len(words)

def book_count_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def book_count_words_sorted(text):
    sorted_list = []
    for ch in text:
        sorted_list.append({"char": ch, "num": text[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list