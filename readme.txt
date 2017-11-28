What I did:

Download Pride and Prejudice text from Project Gutenberg. It's the most popular ebook on their site (as of 11/28/2017). https://www.gutenberg.org/browse/scores/top
so it seems like a good place to start. Download this in plaintext format so that it's easiest to work with. https://www.gutenberg.org/files/1342/1342-0.txt

Edit this text to remove the start and ending Project Gutenberg-added information. This is a bit of copyright information and just some general description of Pride and Prejudice. While I'm sure this information is important, it is not the text of Pride and Prejudice and keeping it there will just mess up the alogorithms. Then, go through and remove all "Chapter X" headers since they are also extraneous.

Tried using the Markovify python package (https://github.com/jsvine/markovify) since it seems like one of the best "batteries included" Markov Chain text generation packages. While the details of how to actually implement text generation with markov chains is cool (see https://aritter.github.io/courses/5525_slides/memm.pdf for more details), for this experiment I just want to see results.

https://github.com/jsvine/markovify contains instructions on some cool Markovify features. I did:

```
import markovify

# Get raw text as string.
with open("/path/to/my/corpus.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(5):
    print(text_model.make_short_sentence(100))
```

and got these 5 "long" sentences:
- He seemed scarcely to be her feelings towards _one_ in that short period saw him till after your mother’s family, though objectionable, was nothing in it by knowing that his character and his intrigues, all honoured with a very desirable partner.                  
- “Then you would be likely to make five shillings any object.                            
- His accompanying them was very much to the officers, Mr. Collins did not quit her room on leaving church to come at all!                                                        
- All connection between us already, that we are all wishing him to pronounce.            
- “I had much rather go in the very day of my stay, but real, though unavailing concern.


and these 3 "short" sentences:
- And you are giving it a case of some minutes, in silence; and, at last, on the same spot.
- Lydia laughed, and said: “Jane, I congratulate her.
- Mr. Bennet, for anything but a day of her life.”
- That _she_ could be pointed out as will shock your relations to hear.”
- Mr. Darcy was the least of receiving them at Longbourn.”

Some observations here:
- All of the generated sentences end in periods. This makes sense, as the training data is theoretically gramatically correct and thus all of its sentences end in periods. This is a fairly formal source text (compared to texts, Facebook posts, etc.).
- The quotation marks feel out of place. And they are, as these sentences are generated without consideration for meaning. `and said: "Jane...`, however, does use a quotation mark correctly, which is pretty cool. Also, opening and closing quotation marks are not aligned consistently.

I tried running this a bunch of times to see if I could get any interesting sentence results. Here were the top 3:
- I _will_ leave him to be ashamed of you!
- Let me take it on any terms other than marriage?
- My dearest Lizzy will, I dare say Kitty is forwarder than either of those?

Final thoughts: most of the generated sentences sounded like giberish. I think a big reason for this was that the probabilities used to generate these only took into account likelihood based on the past few words. If the generated sentences were then compared to the likelihood of it being an English sentence, these might yield better results.
