import os
from pdf2image import convert_from_path
import pytesseract
from langchain_ollama import ChatOllama

pdf_path = "document.pdf"

if not os.path.exists(pdf_path):
    print(f"❌ Error: Could not find '{pdf_path}' in this folder.")
    exit()

print(f"👁️ Scanned PDF detected! Running OCR Image Processing on '{pdf_path}'...")
print("Please wait, converting pages to images and reading text characters...")

try:
    # 1. Convert the PDF pages into flat images
    pages = convert_from_path(pdf_path, 300) # 300 DPI for high accuracy
    
    pdf_text = ""
    # 2. Loop through each page image and extract text via Tesseract OCR
    for i, page_image in enumerate(pages):
        print(f"📸 Reading text from Page {i+1}...")
        page_text = pytesseract.image_to_string(page_image)
        pdf_text += page_text + "\n"

except Exception as e:
    print(f"\n🚨 System Error during OCR processing: {e}")
    print("Make sure you ran 'brew install tesseract poppler' in your terminal!")
    exit()

# --- DIAGNOSTIC TEST ---
print("\n🔍 TEXT DIAGNOSTIC CHECK:")
print(f"Total extracted characters: {len(pdf_text)}")
if len(pdf_text.strip()) == 0:
    print("🚨 ERROR: OCR failed to extract text. The document might be fully encrypted.")
    exit()
else:
    print("--- Snippet of what OCR extracted (First 200 chars) ---")
    print(pdf_text[:200].strip())
    print("-----------------------------------------------------------\n")

print("🤖 Initializing local Llama with expanded context...")
llm = ChatOllama(model="llama3.2", temperature=0, num_ctx=8192)

output_log_path = "ai_analysis_report.txt"
print(f"🚀 Interactive OCR PDF Session Started! Report saves to: '{output_log_path}'\n")

while True:
    user_question = input("❓ Ask about the PDF: ")
    
    if user_question.lower().strip() == 'exit':
        print("👋 Exiting session. Goodbye!")
        break
        
    if not user_question.strip():
        continue

    prompt = f"""
    You are an advanced data assistant analyzing a PDF document. 
    Use the extracted PDF text below to answer the question thoroughly and accurately.
    
    ---
    EXTRACTED PDF CONTENT:
    {pdf_text}
    ---
    
    QUESTION: {user_question}
    """
    
    print("🧠 Thinking...")
    response = llm.invoke(prompt)
    ai_answer = response.content
    
    print(f"\n✨ AI Response:\n{ai_answer}\n")
    print("-" * 50)
    
    with open(output_log_path, "a", encoding="utf-8") as report_file:
        report_file.write(f"Question: {user_question}\n")
        report_file.write(f"Answer:\n{ai_answer}\n")
        report_file.write("-" * 60 + "\n\n")
