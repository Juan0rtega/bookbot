from os import supports_bytes_environ


def main():
    print("--- Begin report of books/frankenstein.txt --- \n")
    file_contents = get_book()
    n_words = get_n_words(file_contents)
    print(f"{n_words}  words found in the document")

    char_count = get_char_count(file_contents)
    sorted_list = parse_dict(char_count)
    for item in sorted_list:
        print(f"The '{item["name"]}' character was found {item["num"]} times")

    print("--- End report ---")

def get_book() -> str:
    with open("./books/frankenstein.txt") as f:
        return f.read()

def get_n_words(text) -> int:
    return len(text.split())

def get_char_count(text) -> dict:
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
    return char_count

def parse_dict(char_count) -> list:
    report_list = []
    for char in char_count:
        if char.isalpha():
            report_list.append(
                    {
                        "name": char,
                        "num": char_count[char] 
                })
    report_list.sort(reverse=True, key=sort_on)
    return report_list

def sort_on(dict):
    return dict["num"]
main()
