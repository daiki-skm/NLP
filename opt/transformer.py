from janome.tokenizer import Tokenizer
import re

def tokenizer_janome(text):
  return [tok for tok in j_t.tokenize(text, wakati=True)]

def preprocessing_text(text):
  # 改行、半角スペース、全角スペースを削除
  text = re.sub('\r', '', text)
  text = re.sub('\n', '', text)
  text = re.sub('　', '', text)
  text = re.sub(' ', '', text)

  # 数字文字の一律「0」化
  text = re.sub(r'[0-9 ０-９]', '0', text)

  return text

def tokenizer_with_preprocessing(text):
  text = preprocessing_text(text)
  ret = tokenizer_janome(text)

  return ret

if __name__ == '__main__':
  j_t = Tokenizer()

  text = '機械学習が好きです。'
  for token in j_t.tokenize(text):
    print(token)

  text = "昨日は とても暑く、気温が36度もあった。"
  print(tokenizer_with_preprocessing(text))