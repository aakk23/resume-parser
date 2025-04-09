
# 📄 Resume Parser (Streamlit App)

A web-based resume parser built using Python and Streamlit. Upload a single PDF or a `.zip` file containing multiple resumes, and extract key information like:

- ✅ Name (email-assisted search-based matching)
- ✅ Email
- ✅ Phone
- ✅ LinkedIn / GitHub / Other URLs
- ✅ Skills
- ✅ Bulk resume parsing (via ZIP upload)
- ✅ Optional export to Google Sheets (if enabled)

---

## 🚀 Demo

> [Live App on Streamlit Cloud](https://resume-parser-aakk.streamlit.app/)  

---

## 📦 Features

| Feature              | Status |
|----------------------|--------|
| Upload PDF or ZIP    | ✅     |
| Name extraction via email match | ✅ |
| Link classification (LinkedIn, GitHub, etc.) | ✅ |
| Skills section parsing + fallback | ✅ |
| Google Sheets export | ✅ (optional setup) |
| Streamlit UI         | ✅     |

---

## 📁 Folder Structure

```
resume-parser/
├── app.py                   # Main Streamlit app
├── resume_parser_v05.py     # Resume parsing logic
├── requirements.txt         # Python dependencies
└── .streamlit/config.toml   # Streamlit settings (optional)
```

---

## ✅ Getting Started (Local)

```bash
git clone https://github.com/aakk23/resume-parser.git
cd resume-parser
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Deploying on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click **"New App"**, connect your GitHub
4. Set `app.py` as the main file
5. Done 🎉

---

## 🔐 (Optional) Google Sheets Export

If you want parsed results saved to Google Sheets:

1. Enable Google Sheets API from [Google Cloud Console](https://console.cloud.google.com)
2. Download `credentials.json` for a service account
3. Add the credentials file securely to your environment
4. Share the target sheet with your service account's email

> *Google Sheets logic is already built into `resume_parser_v05.py`.*

---

## 🧠 Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io)
- [PyMuPDF](https://pymupdf.readthedocs.io)
- [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- gspread (for Google Sheets)

---

## 🙋‍♂️ Author

**Aakkash Aswin**  
🌐 [LinkedIn](https://www.linkedin.com/in/aakkash-aswin)  
💻 [GitHub](https://github.com/aakk23)
