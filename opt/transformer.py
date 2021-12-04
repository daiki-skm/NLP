from janome.tokenizer import Tokenizer

def tokenizer_janome(text):
  return [tok for tok in j_t.tokenize(text, wakati=True)]

if __name__ == '__main__':
  j_t = Tokenizer()
  text = '機械学習が好きです。'
  for token in j_t.tokenize(text):
    print(token)

  print(tokenizer_janome(text))