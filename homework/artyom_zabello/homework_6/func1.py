def word_counter(word: str) -> str:
    """ this function returns a string with
    unique characters and their quantity """
    lst = []
    for index, _ in enumerate(word):
        if word[index] in lst:
            if word[index] != word[index-1] and word[index] != word[index+1]:
                lst.append(word[index])
            else:
                continue
        else:
            lst.append(word[index])
            if word.count(word[index]) > 1:
                if word[index] not in word[index+5:len(word)]:
                    lst.append(word.count(word[index]))
                else:
                    lst.append(word.count(word[index])-1)

    return "".join(map(str, lst))


print(word_counter(input()))
