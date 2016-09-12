from random import choice

with open('C:/Users/Kevin/Downloads/story.txt', 'r') as text:
    words = text.read().split()

def create_dict(input_list):
    # Creates a dict using every two words as a tuple key and the following word as the value
    d = {}    
    for i in xrange(len(input_list)-2):
        d.setdefault((input_list[i], input_list[i+1]), []).append(input_list[i+2])
    return d 
 
def generate_sentence(d):
    # Generates a random markov sentence that will start with a uppercase word
    # and end with a period, question mark, or exclamation mark
    capital_words = [w for w in d.keys() if w[0][0].isupper() and w[0].isalpha()]
    start = choice(capital_words)
    word1, word2 = start[0], start[1]
    sentence = []
    sentence.extend((word1,word2))
    
    while True:
        word3 = choice(d[(word1, word2)])
        sentence.append(word3)
        if word3[-1] in '.!?':
            break
        word1, word2 = word2, word3
 
    return ' '.join(sentence)
    
if __name__ == "__main__":
    d = create_dict(words)
    print generate_sentence(d)
