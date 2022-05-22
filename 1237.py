from difflib import SequenceMatcher
while True:
    try:
        a = input()
        b = input()
        x = SequenceMatcher(None, a, b)
        seq = x.find_longest_match(0, len(a), 0, len(b))
        print(seq.size)
    except:
        break