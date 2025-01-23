def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(character_count(file_contents))

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

def characher_sorter(d):
    pass

def cat_report(w, c):
    pass


main()