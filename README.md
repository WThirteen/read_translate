# read translate
## 中文识别翻译
<h4 align="center">
    <p>
        <a href="https://github.com/WThirteen/read_translate/blob/master/README.md">中文</a> |
        <a href="https://github.com/WThirteen/read_translate/blob/master/README_en.md">English</a>      
    <p>
</h4>

# 原理
* 读取中文语句，语音识别。识别为文本。
* 将中文文本翻译为英文
-------------------------------------
语言识别使用到openai的whisper   
具体使用可看 [whisper](https://github.com/openai/whisper)   

-------------------------------------
翻译使用到hugging face的翻译模型 opus-mt-zh-en  
模型文件可从hugging face下载  [opus-mt-zh-en](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en/tree/main)   
或者在百度网盘中下载 
链接: https://pan.baidu.com/s/1eE5fVBfGSwEZeAeoIerjgg?pwd=eqrn  
提取码: eqrn 



# 配置环境
* 创建虚拟环境
```
conda create -n my_env python=3.10
```
* 激活虚拟环境
```
activate my_env
```
* 安装所使用的库
```
pip install -r requirements.txt
```

# 使用
* 激活虚拟环境
```
activate my_env
```
* 运行
```
python main.py
```
# 新增ui
* 运行
```
python main_ui.py
```
## ui页面如下  
![ui](https://github.com/WThirteen/read_translate/assets/100677199/66a97e24-6560-44db-b082-5b235288f4a4)

