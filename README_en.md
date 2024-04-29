# read translate
## Chinese recognition translation  

<h4 align="center">
    <p>
        <a href="https://github.com/WThirteen/read_translate/blob/master/README.md">中文</a> |
        <a href="https://github.com/WThirteen/read_translate/blob/master/README_en.md">English</a>      
    <p>
</h4>


# Principle
* Read Chinese sentences, speech recognition. Identify as text.
* Translate Chinese text into English
-------------------------------------
Language recognition uses openai's whisper   
Specific use can see [whisper](https://github.com/openai/whisper)   

-------------------------------------
The translation uses a hugging face translation model opus-mt-zh-en   
Model files are available from hugging face download [opus-mt-useful-en](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en/tree/main)   
Or download it in Alibaba Cloud disk   
https://www.alipan.com/s/DMu9ettGzHE
Extraction code: o1y2


# Configure the environment
* Create a virtual environment
```
conda create -n my_env python=3.10
```
* Activate the virtual environment
```
activate my_env
```
* Install the library used
```
pip install -r requirements.txt
```

# Use
* Activate the virtual environment
```
activate my_env
```
* Run
```
python main.py
```
