def func(inp):
    word = list(inp)
    word_for_reverse = word[:]
    word_for_store = word[:]

    word_len = len(word)-1

    word_for_reverse.sort(reverse=True)
    if word == word_for_reverse:
        return "no answer"

    while True:
        for i in range(word_len, 0, -1):
            word[i], word[i-1] = word[i-1], word[i]
            if word_for_store < word:
                return ''.join(word)



for _ in range(int(input())):
    inp = input()
    while inp == '':
        inp = input()
    print(func(inp))
