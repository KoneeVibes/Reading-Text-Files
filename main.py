# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        content = f.read()
        print(content)
    return content


def count_words():
    text = read_file_content(
        "C:/Users/HP/.idle/Reading-Text-Files/story.txt")
    # [assignment] Add your code here
    cleaned_text = text.split()
    wc = {}

    for i in cleaned_text:
        if i in wc:
            wc[i] += 1
        else:
            wc[i] = 1

    print(wc)
    return {"as": 10, "would": 20}
    # return {"as": 10, "would": 20}


read_file_content("C:/Users/HP/.idle/Reading-Text-Files/story.txt")
count_words()
