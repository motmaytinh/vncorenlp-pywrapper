from vncorenlp import VnCoreNLP

# simple usage
nlp = VnCoreNLP("/home/q/Desktop/Workspace/tokenizer/VnCoreNLP-1.1.jar")

sentence = 'xin chào các bạn!'

tokens = nlp.word_tokenizer(sentence)


print(tokens)