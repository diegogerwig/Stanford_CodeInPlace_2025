from collections import OrderedDict

def main():
    words = load_words_from_file("words.txt")

    # Contar palabras manteniendo el orden de aparición
    word_counts = OrderedDict()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Imprimir el histograma respetando el orden original
    for word, count in word_counts.items():
        print_histogram_bar(word, count)


def print_histogram_bar(word, count):
    """
    Imprime una barra del histograma alineada.
    """
    print(f"{word : <8}: {'x' * count}")


def load_words_from_file(filepath):
    """
    Carga palabras desde un archivo en una lista, una por línea.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words


if __name__ == '__main__':
    main()
