from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class Config():
    path="model/opus-mt-zh-en"

    
def load_model():
    config = Config()

    tokenizer = AutoTokenizer.from_pretrained(config.path)
    
    model = AutoModelForSeq2SeqLM.from_pretrained(config.path)
    
    return tokenizer,model 


def IN():
    sentence=input("请输入:")
    return sentence

def translate(text,tokenizer,model):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded

def run():
    print("---load_model---")
    tokenizer,model = load_model()
    print("---中译英---")
    print("输入exit结束")
    while (True):
        text = IN()
        if text == 'exit':

            break
    
        decoded = translate(text,tokenizer,model)

        print(decoded)


if __name__ == '__main__': 
    run()



