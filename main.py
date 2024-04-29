from ans import takeCommand
from translate import load_model,translate
import os

def Run():
    tokenizer,model = load_model()
    text = takeCommand()
    decoded = translate(text,tokenizer,model)
    print('翻译:')
    print(decoded)

if __name__ == "__main__":
    Run()
    os.remove("temp_file.wav")