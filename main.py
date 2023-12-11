with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")

    #Count the number of words
    words = file_contents.split()
    print(len(words)," words found in the document\n")
    
    #Count Characters and symbols in each book
    letters = {}
    for l in file_contents.lower():
        if l not in letters:
            letters[l] = 1
        else:
            letters[l] += 1
    #Report Letters Orrder by Occurence
    for a in sorted(letters, key=letters.get,reverse=True):
        if a.isalpha():
            print("The '",a,"' character was found ",letters[a]," times")
    
    print("--- End report ---")
