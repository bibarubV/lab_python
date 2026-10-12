#!/usr/bin/env python3

import re
from collections import defaultdict

def analyze_text(text, skip=None):
    cmp = lambda x: len(x) >= skip if skip else lambda x: True
    words = list(filter(cmp, re.findall(r"\w+", text, flags=re.UNICODE)))
    word_count = defaultdict(int)
    shortest = words[0].lower()
    longest = words[0].lower()
    for word in words:
        word = word.lower()
        word_count[word] += 1
        shortest = word if len(word) < len(shortest) else shortest
        longest = word if len(word) > len(longest) else longest
    most_frequent = max(word_count, key=word_count.get)
    print("Слова:", words)
    print("Количество слов:", len(words))
    print("Частота каждого слова:", dict(word_count))
    print("Самое частое слово:", most_frequent)
    print("Самое короткое слово:", shortest)
    print("Самое длинное слово:", longest)

def main():
    text = ""
    s = input("Введите текст:\n")
    while s:
        text += s
        s = input()

    print("Анализ текста:")
    analyze_text(text)

    print()
    print("Анализ текста без учета коротких слов:")
    analyze_text(text, 3)

if __name__ == "__main__":
    main()
