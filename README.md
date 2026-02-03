# AI-Financial-News-Analyzer
An AI-powered system for automatically discovering, analyzing, and generating insights from financial news.


## 🚀 Features

- Collects real-time financial news from external APIs  
- Extracts clean article text
- Uses LLMs to:
  - classify news importance  
  - detect sentiment tone  
  - generate concise summaries  
- Filters market-relevant news  
- Generates article/post drafts  
- Stores structured data in Supabase  
- Automated orchestration via n8n  

---

## 🧠 Use Case

Financial news is noisy and time-consuming to analyze manually.

This system helps:

- filter important news  
- quickly understand sentiment  
- generate ready-to-use content drafts  
- structure news data for further analytics  

---

## 🏗 Architecture

Pipeline:

News API  
→ FastAPI service  
→ Text cleaning & extraction  
→ n8n automation workflow  
→ LLM analysis (importance, tone, summary)  
→ Filtering logic  
→ Article draft generation  
→ Supabase storage  

---

## 🛠 Tech Stack

- Python  
- FastAPI  
- n8n  
- Google Gemini (LLM)  
- Supabase  
- REST APIs  

---

## ⚙️  How it works
1.  Click the manual trigger to call the external summarization endpoint, which returns a list of recent stock‑related articles.
2. The raw article text is cleaned, split into separate items and each article’s title, URL and cleaned content are prepared.
3. A Gemini LLM analyzes each article, classifying it as important or unimportant, detecting the sentiment tone, and producing a concise 2‑3 sentence summary.
4. Only articles marked important are passed to a second Gemini model that writes a 200‑300 word engaging post in the detected tone, ending with the source URL.
5. All fields – title, URL, importance, tone, summary and the generated article – are stored in a Supabase table for later use.

---

## 📊 Example Output

Each article is processed into:

- created_at
- title  
- URL  
- importance score  
- sentiment tone  
- summary  
- generated article draft  

Example results are available in sample_output.json

---
