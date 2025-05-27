def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct = 0
    total = len(translations)

    for english_word, spanish_translation in translations.items():
        answer = input(f"What is the Spanish translation for {english_word}? ").strip().lower()
        if answer == spanish_translation:
            print("That is correct!\n")
            correct += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {spanish_translation}.\n")

    print(f"You got {correct}/{total} words correct, come study again soon!")

if __name__ == '__main__':
    main()
