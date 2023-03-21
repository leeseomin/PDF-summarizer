import os
from pdfminer.high_level import extract_text
from tkinter import filedialog, Tk, Label, Button, Text, Scrollbar, messagebox
from summarizer import Summarizer

def read_pdf_file(file_path):
    text = extract_text(file_path)
    return text

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        file_path_label.config(text=file_path)

def process_file():
    if not file_path:
        messagebox.showerror("Error", "Please select a PDF file.")
        return

    text = read_pdf_file(file_path)

    result_text.delete(1.0, "end")
    result_text.insert("end", f"Extracted Text:\n{text}\n")


import torch
from fairseq.models.bart import BARTModel

import spacy


# Load the BART model
bart = BARTModel.from_pretrained('bart.large.xsum', checkpoint_file='model.pt')
bart.to('cpu')
bart.eval()

def summarize_text():
    if not file_path:
        messagebox.showerror("Error", "Please process a PDF file first.")
        return

    text = result_text.get(1.0, "end-1c")

    # Split the text into 
    text_parts = []
    text_length = len(text)
    part_length = text_length // 9
    for i in range(9):
        start = i * part_length
        end = (i + 1) * part_length if i < 8 else text_length
        text_parts.append(text[start:end])

    # Use spaCy to extract named entities from the text
    nlp = spacy.load("en_core_web_sm")

    summaries = []
    for part in text_parts:
        doc = nlp(part)
        entities = set([ent.text for ent in doc.ents])

        # Use BART to summarize the text with max_len_b set to 200
        summary = bart.sample(part, beam=4, lenpen=2.0, max_len_b=200, min_len=55, no_repeat_ngram_size=3)

        # Filter out sentences that do not contain named entities
        summary_lines = summary.split('\n')
        filtered_lines = []
        for line in summary_lines:
            if any(entity in line for entity in entities):
                filtered_lines.append(line)
        summary_text = '\n'.join(filtered_lines)
        summaries.append(summary_text)

    # Combine the summaries
    combined_summary = "\n\n".join(summaries)

    # Display the combined summary in the result_text Text widget
    result_text.delete(1.0, "end")
    result_text.insert("end", "Summary:\n\n")
    result_text.insert("end", "\n".join(combined_summary.split("\n")))
    result_text.insert("end", "\n")




# The rest of the code remains the same


def save_to_file():
    if not file_path:
        messagebox.showerror("Error", "Please process a PDF file first.")
        return

    text = result_text.get(1.0, "end-1c")

    save_file_path = filedialog.asksaveasfilename(initialdir=os.path.expanduser("~"), filetypes=[("Text Files", "*.txt")], defaultextension=".txt")
    if save_file_path:
        with open(save_file_path, 'w', encoding='utf-8') as file:
            file.write(text)

root = Tk()
root.title("PDF Summarizer")
root.geometry("1200x800")

file_path_label = Label(root, text="No file selected.", wraplength=800, font=("Helvetica", 14))
file_path_label.pack()

browse_button = Button(root, text="Browse PDF", command=browse_file, font=("Helvetica", 14), height=2, width=20)
browse_button.pack(pady=10)

process_button = Button(root, text="Process PDF", command=process_file, font=("Helvetica", 14), height=2, width=20)
process_button.pack(pady=10)

summarize_button = Button(root, text="Summarize Text", command=summarize_text, font=("Helvetica", 14), height=2, width=20)
summarize_button.pack(pady=10)

save_button = Button(root, text="Save to File", command=save_to_file, font=("Helvetica", 14), height=2, width=20)
save_button.pack(pady=10)

result_text = Text(root, wrap="word", height=15, font=("Helvetica", 14))
result_text.pack(pady=10)

scrollbar = Scrollbar(root, command=result_text.yview)
scrollbar.pack(side="right", fill="y")

result_text.config(yscrollcommand=scrollbar.set)

file_path = None

root.mainloop()
