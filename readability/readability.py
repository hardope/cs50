# gets text input
text = input("Text: ")
letters = 0
words = 1
sentence = 0
# counts letters
for i in text:
    if (i.isalpha()):
        letters += 1
# counts words
for j in text:
    if (j == " "):
        words += 1
# counts sentences
for l in text:
    if (l == '.' or l == '!' or l == '?'):
        sentence += 1

L = (letters / words) * 100
S = (sentence / words) * 100
# calculates grade
d = round(0.0588 * L - 0.296 * S - 15.8)

if d < 1:
    print("Before Grade 1")
elif d > 16:
    print("Grade 16+")
else:
    print(f"Grade {d}")