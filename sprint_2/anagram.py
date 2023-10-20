def anagrams(word, words):
    anagrams = []
    chars_list = list(word)
    chars_sorted = sorted(chars_list) 

    for ocurrence in words:
        l = [chars for chars in ocurrence]
        l_sorted = sorted(l)
        if chars_sorted == l_sorted:
            anagrams.append(ocurrence)
        
    return anagrams

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada', 'abbb', 'aaab']))