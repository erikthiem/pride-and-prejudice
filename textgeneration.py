import markovify

# Get raw text 
with open("pride-prejudice-edited.txt") as f:
    pride_prejudice_text = f.read()
with open("starwars4.txt") as f:
    star_wars_4_text = f.read()

# Build the models
pride_prejudice_text_model = markovify.Text(pride_prejudice_text)
star_wars_4_text_model = markovify.Text(star_wars_4_text)

# Combine them!
combined_text_model = markovify.combine([ pride_prejudice_text_model, star_wars_4_text_model ], [ 1, 1 ])

for i in range(10):
    print(combined_text_model.make_short_sentence(120))
    print("")
