# Counts words in a string


def main():

    # Input a sentence
    sentence = input("Enter a sentence: ")
    # Get the amount of words
    words = countWords(sentence)

    # Get average word length.
    length = avgLength(sentence)

    print(f"{words} words. Words were, on average, {length} characters long.")


def countWords(sentence):
    words = sentence.split()
    wordCount = len(words)
    return wordCount


def avgLength(sentence):
    totalChars = 0
    words = sentence.split()
    for i, word in enumerate(words):
        totalChars += len(word)

    return round(totalChars / len(words), 2)


if __name__ == "__main__":
    main()
