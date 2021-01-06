import string
import timeit
start = timeit.timeit()

#Title simplifier:
def simplifier(words):
    """Removes special characters."""    
    for character in string.punctuation:
        words = words.replace(character, "")
    return(words)

#Open note:
notes = input("Name of the note file: \n")
if len(notes) < 1: notes = "My clippings.txt" 

with open(notes, errors="ignore") as note_file:

#Convert file into a list:
    note_list = []
    for line in note_file:
        note_list.append(line.rstrip())

#Extract book tiltes:
    book_titles = set()
    for i in range(len(note_list)):
        if note_list[i].startswith("- Your"):
            book_title = note_list[i-1]
            book_titles.add(book_title)

#Create separate note files:
    for title in book_titles:
        with open ("{}.txt".format(simplifier(title)), "w") as fhandle:
            for i in range(len(note_list)):
                #pop for removing lines from the list
                j = i
                if note_list[i].startswith("{}".format(title)):
                    while True:
                        j += 1
                        if note_list[j].startswith("- Your"):
                            continue
                        elif note_list[j].startswith("==="):
                            fhandle.write("\n")
                            fhandle.write(60*"=")
                            break
                        else:
                            fhandle.write(note_list[j])
                            fhandle.write("\n")
                else:
                    continue

end = timeit.timeit()
print("Time elapsed: ", end - start)