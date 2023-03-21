# PDF-summarizer

pdf 에서 text 추출후에 이것을 요약하는 프로그램.
A program that extracts text from a PDF and summarizes it afterwards. :
It is a summary process that divides the given text into 9 parts, summarizes each part, and then combines them. It is suitable for paper summarization.


  <br/> <br/><br/> 
###  Dependency (Tested on an M1 Mac) : cpu version

``` conda install pytorch torchvision torchaudio -c pytorch ```

``` pip install pdfminer.six``` 

```git clone https://github.com/pytorch/fairseq```

```cd fairseq```

```CFLAGS="-stdlib=libc++" pip install --editable ./``` 


 <br/><br/> 
 
### Run Code 

```python V_07.py```




  <br/>
 <br/><br/> 

### Credit

BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension :https://github.com/facebookresearch/fairseq/blob/main/examples/bart/README.md

pdfminer.six  :  https://github.com/pdfminer/pdfminer.six 


