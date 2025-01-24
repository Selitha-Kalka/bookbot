book = "books/frankenstein.txt"

def main():
    with open(book) as f:
        file_contents = f.read()
        word_c = word_count(file_contents)
        char_count = dict_scrub(character_count(file_contents))
        char_count.sort(reverse=True, key=sort_on)

        cat_report(word_c, char_count)

def word_count(s):
    words = s.split()
    return len(words)

def character_count(s):
    count = {}
    j = s.lower()
    for i in j:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

def sort_on(dict):
    return dict["num"]

def cat_report(w, c):
    print(f"Beginning report on: {book}...")
    print(f"{w} words found in the document.")
    for i in range(len(c)):
        print(f"The '{c[i]["alpha"]}' character was found {c[i]["num"]} times.")
    print("--- End Report ---")

def dict_scrub(d):
    clean = []
    for i in d:
        if i.isalpha():
            clean.append({"alpha" : i, "num" : d[i]})
    return clean

main()