import re
from pdfminer.high_level import extract_text


def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None


def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-\(\)]{7,}\d', text)
    return match.group(0) if match else None


def extract_social_links(text):
    return re.findall(r'(https?://[^\s]+)', text)


def extract_name(text):
    # Assumes name is in first 3 lines and avoids summary-like phrases
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    for line in lines[:3]:
        if 2 <= len(line.split()) <= 5 and not re.search(r'\b(summary|email|phone|contact)\b', line, re.I):
            return line
    return None


def extract_skills(text):
    skills = set()
    # A basic list of skills (extendable)
    skill_keywords = [
        'python', 'java', 'sql', 'excel', 'power bi', 'tableau',
        'machine learning', 'data analysis', 'communication',
        'teamwork', 'leadership', 'javascript', 'html', 'css'
    ]
    for keyword in skill_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text, re.I):
            skills.add(keyword.title())
    return sorted(skills)


def parse_resume(filepath):
    """
    Main parser function: Extracts structured data from a resume PDF.
    Returns a dictionary with extracted information.
    """
    text = extract_text(filepath)

    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Social Links": extract_social_links(text),
        "Skills": extract_skills(text)
    }
