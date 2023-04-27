import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())

def flip_word(word: str):
    return_word = []
    for i in range(len(word)-1, -1, -1):
        return_word.append(word[i])
    return return_word

for _ in range(N):
    sentence = sys.stdin.readline().split()
    flipped = []
    for i in range(len(sentence)):
        word = sentence[i]
        flipped_word = flip_word(word)
        flipped.append(''.join(flipped_word))
    print(' '.join(flipped))