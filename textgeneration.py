import markovify

# Get raw text as string.
with open("pride-prejudice-edited.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print five randomly-generated sentences of no more than 100 characters
for i in range(5):
    print(text_model.make_short_sentence(100))

# Print out a bunch of random sentences
for i in range(50):
    print(text_model.make_short_sentence(100))
