# PDF-summarizer

pdf 에서 text 추출후에 이것을 요약하는 프로그램.  논문요약등에 활용가능. <br/> 
A program that extracts text from a PDF and summarizes it afterwards. :<br/> 
It is a summary process that divides the given text into 9 parts, summarizes each part, and then combines them. It is suitable for paper summarization.

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
 
### Run Code 

```python V_072.py```

![대표](https://github.com/leeseomin/PDF-summarizer/blob/main/pic/2.png)



  <br/>
 <br/><br/> 

### Credit

BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension :https://github.com/facebookresearch/fairseq/blob/main/examples/bart/README.md

pdfminer.six  :  https://github.com/pdfminer/pdfminer.six 

spaCy : https://github.com/explosion/spaCy
