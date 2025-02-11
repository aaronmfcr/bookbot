def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file, "r") as f:
        file_contents = f.read()

    word_count =count(file_contents)
    char_count = countc(file_contents)
    report_list = report(word_count, char_count)

def count(text):
    words = text.split()
    return len(words)

def countc(text):
    dictionary = {}
    for char in text:
        char = char.lower()
        dictionary[char] = dictionary.get(char, 0) + 1
    return dictionary
def sort_on(dict):
    return dict["count"]

def report(word_count, char_count):
    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
           char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for char_dict in char_list:
        print (f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    print("--- End report ---")
main()