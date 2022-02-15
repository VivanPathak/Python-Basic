Context = "A week ago a friend invited a couple of other couples over for dinner. Eventually, the food (but not the wine) was cleared off the table for what turned out to be some fierce Scrabbling. Heeding the strategy of going for the shorter, more valuable word over the longer cheaper word, our final play was “Bon,” which–as luck would have it!–happens to be a Japanese Buddhist festival, and not, as I had originally asserted while laying the tiles on the board, one half of a chocolate-covered cherry treat. Anyway, the strategy worked. My team only lost by 53 points instead of 58"


words = Context.split()


wordcount = {}

for word in words:

    if word in wordcount:

        wordcount[word] += 1

    else:

        wordcount[word] = 1

for word, count in wordcount.items():
    print(word, ":", count)

