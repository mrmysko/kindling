# Counts words in a string


def main():

    # Input a sentence
    sentence = input("Enter a sentence: ")
    # Get the amount of words
    words = count_words(sentence)

    # Get average word length.
    length = avg_length(sentence)

    print(f"{words} words. Words were, on average, {length} characters long.")


def count_words(sentence):
    words = sentence.split()
    wordCount = len(words)
    return wordCount


def avg_length(sentence):
    total_chars = 0
    words = sentence.split()
    for i, word in enumerate(words):
        total_chars += len(word)

    return round(total_chars / len(words), 2)


if __name__ == "__main__":
    main()
