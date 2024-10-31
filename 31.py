import random

# Набор слогов для генерации слов
syllables = ["бо", "ла", "ро", "да", "ми", "ли", "та", "по", "ли", "ва", "сле", "зо", "ша", "га", "ну", "ку", "пе", "да"]
# Набор предлогов и частиц
prepositions = ["в", "на", "по", "и", "а", "с", "без", "через", "для", "от", "за", "из-за"]

def generate_word():
    word = "".join(random.choice(syllables) for _ in range(random.randint(2, 5)))
    return word.capitalize()

def generate_sentence():
    sentence = []
    for _ in range(random.randint(3, 7)):
        if random.random() < 0.3:  # шанс добавить предлог
            sentence.append(random.choice(prepositions))
        sentence.append(generate_word())
    return " ".join(sentence) + random.choice(["!", ".", "?"])

def generate_text(num_sentences=5):
    return " ".join(generate_sentence() for _ in range(num_sentences))

# Пример вывода текста
print(generate_text())
