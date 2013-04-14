from collections import Counter, defaultdict

wordlist = ['red', 'yellow', 'blue', 'red', 'green', 'blue', 'blue', 'yellow']

# count the frequency of occurrence of each word in list with that count
wordfreq = Counter(wordlist)

# invert the wordfreq dictionary so keys are
# frequency of occurrence and values are the words
freqword = defaultdict(list)
for word, freq in wordfreq.items():
    freqword[freq].append(word)

# print in order of occurrence
occurrences = freqword.keys()
occurrences.sort()
for freq in occurrences:
    freqword[freq].sort() # sort words in list
    print 'count {}: {}'.format(freq, freqword[freq])

# outputs
# count 1: ['green']
# count 2: ['red', 'yellow']
# count 3: ['blue']