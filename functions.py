import random


hedges = ("please tell me more",
          "I want to know more about you. ",
          "Please continue. ")
qualifiers = ("Why do you say that: ",
              "You seem to think that ",
              "Can you explain why: ",
              )
replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours"}


def replay(sentence):
    """Build and return to a sentence"""
    probability = random.randint(1,4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)


def changePerson(sentence):
    words = sentence.split()
    reply_words = []
    for word in words:
        reply_words.append(replacements.get(word, word))
    return " ".join(reply_words)


def main():
    print()
    print()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("Hi how your you hop you are well today.  ")
    print("What can I do for you? ")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "STOP":
            print("Have a nice day! ")
            break
        print(replay(sentence))


if __name__ == "__main__":
    main()
