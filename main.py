from ans import takeCommand
from translate import load_model,translate
import os

def Run():
    tokenizer,model = load_model()
    seq = 1
    while True:
        print(str(seq)+':')
        text = takeCommand()
        decoded = translate(text,tokenizer,model)
        print('翻译:')
        print(decoded)
        seq =  seq + 1
        os.remove("temp_file.wav")

if __name__ == "__main__":
    Run()
    