import sys
from itertools import product
from nltk.corpus import words

words = set(words.words())

# Takes in a list of letters, first letter is the letter that must be used.
def main(letters):
  l = letters.strip('[]').split(',')
  reqL = l[0];
  l = l[1:]

  wordList = []
  getCombos(l, reqL, wordList , 4)

  print(wordList)
  for w in wordList:
    if (isPanagram(w, l)):
      print("panagram: ", w)


def getCombos(letters, reqL, wordList, minL):
  print(letters)
  if (len(letters) < minL):
    return

  l = letters[:]
  l.append(reqL)
  for length in range(minL, 10):
    newWs = [''.join(c) for c in product(l, repeat=length)]
    wordList.extend(filter(lambda x: x in words and reqL in x, newWs))

  # # Remove one letter and recurse down
  # for i in range(len(letters)):
  #   newL = letters[0: i] + letters[i+1:]
  #   getCombos(newL, reqL, wordList, minL)

# Returns if word is panagram
def isPanagram(word, letters):
  for l in letters:
    if (l not in word):
      return False
  return True

if __name__ == "__main__":
  main(sys.argv[1])


