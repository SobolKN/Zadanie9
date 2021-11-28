def main():
  sentence = str(input().lower()).split()
  print(sort_sentence(sentence))

def sort_sentence(sentence):
  sentence = sorted(sentence, key=len)
  sentence[0] = sentence[0].title()
  sentence = " ".join(sentence)
  return sentence

if __name__ == "__main__":
  main()
