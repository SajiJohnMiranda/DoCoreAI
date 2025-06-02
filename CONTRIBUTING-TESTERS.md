# 🧪 Contributing as a Tester

Thank you for your interest in testing **DoCoreAI**!  
Your feedback is vital to improving our platform and shaping the future of intelligent prompt optimization.

> 💡 DoCoreAI is licensed under **CC BY-NC-ND 4.0**, which restricts direct code contributions or modifications.  
> However, **we welcome feedback, test results, and creative feature ideas from our testers**.

---

## 🎁 Free Pro Plan for Valid Testers

We're offering **complimentary Pro plan access** (SaaS version of DoCoreAI) to testers who meet the following criteria:

✅ Sign up for the **free trial plan** at [https://docoreai.com/register/](https://docoreai.com/register/)  
✅ Perform real-world testing using your own prompts and scenarios  
✅ Submit any **valid bugs**, **creative feature suggestions**, or **meaningful usability feedback**

📨 Send your feedback to **info@docoreai.com** with subject: `Testing Feedback – Pro Plan Request`

---

## 🚀 What You’ll Be Doing

- 🧠 Compare DoCoreAI's responses with standard LLM outputs  
- 🧪 Evaluate prompt optimization accuracy, token savings, and efficiency  
- 💡 Suggest feature ideas or interface improvements  
- 🐞 Report any issues, bugs, or edge cases

---

## 📝 How to Get Started

### 1. Install the CLI Tester

Install Python if not already installed: https://www.python.org/downloads/

In your terminal, run:

```
pip install docoreai

```
---

Download sample test script: https://github.com/SajiJohnMiranda/DoCoreAI/blob/main/tests/Quick%20Test/test.py

---

### Create a .env file in your test directory:

```
# .env
OPENAI_API_KEY="your-openai-api-key"
GROQ_API_KEY="your-groq-api-key"
MODEL_PROVIDER="openai"         # Choose 'openai' or 'groq'
MODEL_NAME="gpt-3.5-turbo"      # Or use groq model: gemma2-9b-it

```

### Run Your Test
```
python test.py

```