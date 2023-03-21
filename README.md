# PDF-summarizer

pdf 에서 text 추출후에 이것을 요약하는 프로그램.  논문요약등에 활용가능. <br/> 
A program that extracts text from a PDF and summarizes it afterwards. :<br/> 
It is a summary process that divides the given text into 9 parts, summarizes each part, and then combines them. 
<br/>
Text extraction can cover hundreds of pages. 텍스트추출은 수백페이지도 가능.
Summarize is appropriate for papers. 텍스트요약기능은 논문등 길지않은 pdf문서들에 적합.
<br/>  Summarization takes a bit longer to process. 요약기능은 처리시간이 다소 오래걸립니다.
![대표](https://github.com/leeseomin/PDF-summarizer/blob/main/pic/1.png)



  <br/> <br/><br/> 
###  Dependency (Tested on an M1 Mac) : cpu version


``` conda install pytorch torchvision torchaudio -c pytorch ```

```pip install pdfminer.six``` 

```pip install spacy```

fairseq install <br/>

```git clone https://github.com/pytorch/fairseq```

```cd fairseq```

```CFLAGS="-stdlib=libc++" pip install --editable ./``` 


 <br/><br/> 
 
 
### Key Features


1.Extract text from PDF and save as a different name txt file.

2.Extract text from PDF, summarize and save as a different name txt file.

1. PDF에서 텍스트를 추출하여 다른 이름의 txt 파일로 저장합니다.

2. PDF에서 텍스트를 추출하고 요약하여 다른 이름의 txt 파일로 저장합니다.

 
 
 
### Run Code 

```python V_072.py``` 

![대표](https://github.com/leeseomin/PDF-summarizer/blob/main/pic/2.png)



  <br/>
 <br/><br/> 



### Limitation

Large PDF files produce strange results when using the text summarization function.

용량큰 pdf파일은 텍스트요약시에 이상한 결과를 배출.


###  To Do

ADD the T5X algorithm  (https://github.com/google-research/t5x)


### Credit

BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension :https://github.com/facebookresearch/fairseq/blob/main/examples/bart/README.md

pdfminer.six  :  https://github.com/pdfminer/pdfminer.six 

spaCy : https://github.com/explosion/spaCy
