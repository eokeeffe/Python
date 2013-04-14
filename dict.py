import re,collections
def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

def union(*dicts):
	return dict(sum(map(lambda dct: list(dct.items()), dicts), []))

NWORDS1 = train(words(file('dictionary.dat').read()))
NWORDS2 = train(words(file('wordsEN.txt').read()))

NWORDS = union(NWORDS1,NWORDS2)

f = open("dictionary.dat","w")
for word in sorted(NWORDS.iterkeys(), reverse=False):
	f.write(word)
	f.write("\n")
f.close()