import PyPDF2
import spacy
import os
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ''

def analyze_document(text, sections):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    analysis = {}
    for section in sections:
        analysis[section] = [sent.text for sent in doc.sents if section.lower() in sent.text.lower()]
    return analysis

def get_embeddings(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings

def calculate_semantic_similarity(text1, text2, model, tokenizer):
    embeddings1 = get_embeddings(text1, model, tokenizer)
    embeddings2 = get_embeddings(text2, model, tokenizer)
    similarity = cosine_similarity(embeddings1, embeddings2)
    return similarity[0][0]

def generate_detailed_report(analysis_doc1, analysis_doc2, similarity_results, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("### Detailed Similarity Report ###\n\n")
        for section, similarity in similarity_results.items():
            file.write(f"Section: {section}\n")
            file.write(f"Semantic Similarity: {similarity * 100:.2f}%\n\n")
            file.write("Content from FEMSA:\n")
            for sentence in analysis_doc1.get(section, []):
                file.write(f"- {sentence}\n")
            file.write("\nContent from FedEx:\n")
            for sentence in analysis_doc2.get(section, []):
                file.write(f"- {sentence}\n")
            file.write("\n\n")

def main():
    pdf_path_doc1 = os.path.join('pyProyects', 'randomFemsa', 'EthicsDocs', 'FEMSA-Code-of-Ethics.pdf')
    pdf_path_doc2 = os.path.join('pyProyects', 'randomFemsa', 'EthicsDocs', 'FEDEXCodeConduct-English.pdf')
    
    sections_doc1 = ['our people', 'our resources', 'culture of lawfulness', 'ethical compliance system']
    
    text_doc1 = extract_text_from_pdf(pdf_path_doc1)
    text_doc2 = extract_text_from_pdf(pdf_path_doc2)
    
    analysis_doc1 = analyze_document(text_doc1, sections_doc1)
    analysis_doc2 = analyze_document(text_doc2, sections_doc1)
    
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    
    similarity_results = {}
    for section in sections_doc1:
        text1 = ' '.join(analysis_doc1.get(section, []))
        text2 = ' '.join(analysis_doc2.get(section, []))
        similarity = calculate_semantic_similarity(text1, text2, model, tokenizer)
        similarity_results[section] = similarity
    
    generate_detailed_report(analysis_doc1, analysis_doc2, similarity_results, 'detailed_similarity_report.txt')
    
    print("Detailed similarity report saved to file.")

if __name__ == "__main__":
    main()
