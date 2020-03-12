def find_anagrams(word, candidates):
    return [i for i in candidates if is_anagram(word, i)]


def is_anagram(word, candidate):
    # verify anagram
    if len(word) != len(candidate) or word.lower() == candidate.lower():
        return False
    for letter in word:
        if letter.lower() not in candidate.lower():
            return False
        # no repeat letter
        index = candidate.lower().index(letter.lower())
        if len(candidate) > index:
            candidate = candidate[:index] + candidate[index + 1:]
        else:
            candidate = candidate[:index]
    return True
