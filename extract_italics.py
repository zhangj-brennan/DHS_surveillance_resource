from docx import Document

doc = Document("DHS interior surveillance resource - FINAL pre legal review (2).docx")  # Change to your filename

italic_phrases = []

for para in doc.paragraphs:
    current = ""

    for run in para.runs:
        if run.italic:
            current += run.text
        else:
            if current.strip():
                italic_phrases.append(current.strip())
            current = ""

    if current.strip():
        italic_phrases.append(current.strip())

# Remove duplicates while preserving order
seen = set()
unique_phrases = []

for phrase in italic_phrases:
    if phrase not in seen:
        seen.add(phrase)
        unique_phrases.append(phrase)

for phrase in unique_phrases:
    print(phrase)