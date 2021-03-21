from urllib.request import urlopen

# we are going to get a bytes objects not string
# because HTTP send us data as raw bytes

story = urlopen("http://sixty-north.com/c/t.txt")
story_words = []

for line in story:
    line_words = line.split()
    for word in line_words:
        word = word.decode("utf-8")
        story_words.append(word)

story.close()
print(story_words)