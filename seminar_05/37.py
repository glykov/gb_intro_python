"""
Напишите программу, удаляющую из текста все слова, содержащие "абв".
"""
with open("words.txt", "r", encoding="utf-8") as fin:
    for line in fin:
        words = line.split()
        for word in words:
            if "абв" in word:
                words.remove(word)
        sentence = " ".join(words)
        print(f"{sentence}")