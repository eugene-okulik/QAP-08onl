def word_counter(word: str) -> str:
    """ this function returns a string with
    unique characters and their number """
    lst = []
    for i in range(len(word)):
        if word[i] in lst:
            if word[i] != word[i-1] and word[i] != word[i+1]:
                lst.append(word[i])
            else:
                continue
        else:
            lst.append(word[i])
            if word.count(word[i]) > 1:
                if word[i] not in word[i+5:len(word)]:
                    lst.append(word.count(word[i]))
                else:
                    lst.append(word.count(word[i])-1)

    return "".join(map(str, lst))


print(word_counter(input()))
