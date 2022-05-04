import random

def noun_plural():
    nouns = ['люди', 'животные', 'белки', 'книги', 'истории', 'программы', 'женщины']
    return random.choice(nouns)

def quantifiers(main_noun):
    quantifiers = ['Некоторые', 'Все']
    return random.choice(quantifiers) + ' ' + main_noun

def verb_plural(subject):
    verbs_plural = ['думают', 'знают', 'пишут', 'говорят']
    return subject + ' ' + random.choice(verbs_plural)

def noun_singular():
    nouns = ['кошка', 'стол', 'погода', 'планета', 'мужчина', 'ребенок', 'чашка']
    return random.choice(nouns)

def verb_singular(subj):
    verbs_singular = ['предпочитает', 'собирается', 'хочет', 'будет', 'ненавидит', 'любит']
    return subj + ' ' + random.choice(verbs_singular)

def verb_infinitive(verb):
    verbs_infinitive = ['читать', 'бегать', 'плавать', 'разговаривать', 'прыгать']
    return verb + ' ' + random.choice(verbs_infinitive)

def subject():
    words = ['всё это', 'это']
    return random.choice(words)

def linking_words(subj):
    linking_word = ['однако', 'но']
    return random.choice(linking_word) + ' ' + subj

def predicate(words):
    predicate_words = ['неправда', 'ложь', 'вздор', 'выдумка','заблуждение']
    return words + ' ' + random.choice(predicate_words)

def random_sentence():
    sentence = verb_plural(quantifiers(noun_plural())) + ', что ' + verb_infinitive(verb_singular(noun_singular())) + ', ' + predicate(linking_words(subject())) + '.'
    return sentence

def main():
    text = random_sentence()
    print(text)

if __name__ == '__main__':
    main()


