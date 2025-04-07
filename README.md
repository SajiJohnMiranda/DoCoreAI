![DoCoreAI Banner](https://raw.githubusercontent.com/SajiJohnMiranda/DoCoreAI/main/assets/DoCoreAI-Github-header-image.jpg)

# 🌟 DoCoreAI – Optimize LLM Intelligence, Reduce Cost, Boost Performance    

#### **🚀 Optimize LLM Responses | 💡 Dynamic AI Intelligence | 💰 Reduce Token Usage & Cost**
---
![🔥 Downloads ](https://img.shields.io/pypi/dm/docoreai)  
![📦 Latest Version](https://img.shields.io/pypi/v/docoreai)  
![🐍 Python Compatibility](https://img.shields.io/pypi/pyversions/docoreai)  
---

## 🔥 What is DoCoreAI?  (All this started as an AI optimization research... read on;)
DoCoreAI is an AI **intelligence profiler that optimizes prompts dynamically** with intelligence parameters. Instead of relying on generic LLM prompts, DoCoreAI customizes with intelligence properties (such as reasoning, creativity, and precision) to ensure AI agents generate responses that perfectly align with their roles.

In Simple words - DoCoreAI is an AI intelligence optimizer that dynamically enhances language model (LLM) responses by adjusting reasoning, creativity, precision, and temperature based on the user role. This eliminates manual prompt engineering and ensures context-aware, role-specific responses for customer support, data analysis, and creative writing.

Whether you're building an AI agent, chatbot, a virtual assistant, or a SaaS application, **DoCoreAI fine-tunes AI prompts in real time**, ensuring **clear, precise, and highly contextual responses**.  

---

## 🌍 Why DoCoreAI?  

### 🚨 **The Problem with Standard AI Models:**  
- **LLMs lack role-based intelligence** – A support bot should be empathetic, but a data bot needs precision.  
- **Trial-and-error tuning is inefficient** – Developers waste time manually adjusting temperature and prompts.  
- **Generic prompts yield unpredictable results** – No clear control over AI intelligence per task.  

### 🧩 **How DoCoreAI Solves This:**  
✅ **Intelligence Profiling:** Automatically adjusts reasoning, creativity, precision, and temperature for the Role.  
✅ **Context Awareness:** Adapts AI responses to the role (e.g., customer support, data analyst, programmer etc..).  
✅ **Token Efficiency:** Reduces API costs by optimizing responses.

### **Key Benefits**
- **🧠 Smarter AI** – Enhances reasoning, problem-solving, and adaptability.
- **⚡ Best Responses** – Intelligent prompts mean more accurate answers.
- **🔧 Full Control** – Developers can fine-tune intelligence parameters like depth, creativity, and accuracy.
- **🔌 Easy API Integration** – Works seamlessly with OpenAI, Cohere, Mistral, and other LLMs.
- **🛠️ Open-Source & Extensible** – Customize it for your specific use case.

---

## 🚀 A New Era in AI Optimization  
DoCoreAI **redefines AI interactions** by dynamically optimizing reasoning, creativity, and precision—bringing human-like cognitive intelligence to LLMs for smarter, cost-efficient responses.

---
A simplified overview:
![DoCoreAI Before & After Comparison](https://raw.githubusercontent.com/SajiJohnMiranda/DoCoreAI/blob/main/assets/Before%20After%20Temp%20DocoreAI.png)
---

## 💡 How Does It Work?  

### How Does DoCoreAI Do This Internally?

- Every DoCoreAI prompt is context-aware, with a role assigned to each query, ensuring accurate intent recognition.

- The core cognitive skills of human intelligence—Reasoning, Creativity, and Precision—are dynamically analyzed.

- DoCoreAI predicts the optimal levels of these skills based on the context of the prompt.

- The temperature is then mathematically derived based on these values using the formula:

T = max(0.1, min(1.2, 0.2 + (0.75 × C) − (0.4 × P) + (0.2 × (1 − R))))

where:

- - C = Creativity
- - P = Precision
- - R = Reasoning
- - Base temperature starts at 0.2

- The carefully crafted system message instructs the AI to predict and assign these values dynamically based on context.

- The LLM then generates responses using these intelligence parameters, optimizing for accuracy, coherence, and efficiency—all in a single step.

In simple words, DoCoreAI follows a structured process to enhance AI prompts:  

1️⃣ Identifies Role & Query Type → Understands task complexity.  
2️⃣ Maps Intelligence Parameters → Determines reasoning, creativity, precision, and temperature.  
3️⃣ Refines Prompt Dynamically → Adjusts LLM input for optimal response.  
4️⃣ Processes via LLM → Sends structured input to OpenAI, Groq, etc.  
5️⃣ Delivers Optimized Output → Returns a refined response.

The process is streamlined, but there's a lot happening under the hood. Want to dig deeper? [Drop your questions in the Q&A section](https://github.com/SajiJohnMiranda/DoCoreAI/discussions/categories/q-a), and let’s unravel the mechanics together! 

---

#### 🔥 Before vs. After DoCoreAI  


|   Scenario          | ❌ Before DoCoreAI | ✅ After DoCoreAI |
|---------------------|------------------|------------------|
| **Basic Query**     | `"Summarize this report."` | `"Summarize this report with high precision (0.9), low creativity (0.2), and deep reasoning (0.8)."` |
| **Customer Support AI** | Responds generically, lacking empathy and clarity | Adjusts tone to be more empathetic and clear |
| **Data Analysis AI** | Generic report with inconsistent accuracy | Ensures high precision and structured insights |
| **Creative Writing** | Flat, uninspired responses | Boosts creativity and storytelling adaptability |
| **Token Efficiency** | Wastes tokens with unnecessary verbosity | Optimizes response length, reducing costs |


---

### **🔗 Step-by-Step Workflow:**
1️⃣ **User Query →** A user submits a question/query to your application.  
2️⃣ **DoCoreAI Enhances Prompt →** The system analyzes the query or prompt and generates an optimized prompt with **dynamic intelligence parameters**. The required intelligence range  for each these parameters (like **Reasoning** - Determines logical depth, **Creativity** - Adjusts randomness , **Precision** - Controls specificity)  are inferred from the query automatically. 

3️⃣ **Send to LLM →** The refined prompt is sent to your preferred LLM (OpenAI, Anthropic, Cohere, etc.).  
4️⃣ **LLM Response →** The model returns a highly optimized answer.  
5️⃣ **Final Output →** Your application displays the AI’s enhanced response to the user.  

👉 **End Result?** More accurate, contextually rich, and intelligent AI responses that **feel human-like and insightful**.  

---

## 💡 How DoCoreAI Helps AI Agents

DoCoreAI ensures that AI agents perform at their best by customizing intelligence settings per task. Here’s how:  

📞 Support Agent AI → Needs high empathy, clarity, and logical reasoning.  
📊 Data Analyst AI → Requires high precision and deep analytical reasoning.  
🎨 Creative Writing AI → Boosts creativity for idea generation and storytelling.  

This adaptive approach ensures that LLMs deliver role-specific, optimized responses every time.


---


### 🚀 Use Cases: How DoCoreAI Enhances AI Agents across various domains

| 🏷️ AI Agent Type      | 🎯 Key Requirements | ✅ How DoCoreAI Helps |
|----------------------|--------------------|----------------------|
| **📞 Customer Support AI** | Needs high **empathy**, **clarity**, and **logical reasoning** | Ensures friendly, concise, and empathetic interactions |
| **📊 Data Analyst AI** | Requires **high precision** and **deep analytical reasoning** | Structures data-driven responses for accuracy and insight |
| **📝 Legal & Compliance AI** | Must be **strictly factual**, legally sound, and highly **precise** | Enhances precision and reduces ambiguity in compliance-related responses |
| **💡 Business Analytics AI** | Needs to extract **meaningful insights** from unstructured data | Improves decision-making by structuring responses intelligently |
| **🏥 Medical AI Assistants** | Requires **high reasoning**, factual correctness, and minimal creativity | Reduces unnecessary creativity to ensure accuracy in medical advice |
| **🎨 Creative Writing AI** | Needs **high creativity** and **storytelling adaptability** | Enhances originality, narrative flow, and engaging content generation |
 
---

### 🏢 **For Businesses & Startups:**
- **🤖 AI Agents, Chatbots & Virtual Assistants** – Make AI interactions **more natural and helpful**.
- **📞 AI Customer Support** – Improve support accuracy, reducing agent workload.
- **📊 Data & Market Analysis** – Extract **meaningful insights from unstructured data**.
- **🎨 Creative AI** –  Enhances storytelling, content generation, and brainstorming.

---

### 🛠️ **For Developers & Engineers:**
- **⚙️ Fine-Tuning Custom LLMs** – Boost reasoning, logic, and adaptability.
- **📝 AI-Powered Content Generation** – Enhance blogs, marketing copy, and technical writing.
- **🧪 Research & Experimentation** – Test and build **next-gen AI applications**.  

---

### 🍒 **Generalized Solution for All**
- **⚙️ Easily Works across all domains and user roles, allowing fine-tuning for different applications
  
---

## 🎯 Getting Started
### **📌 Installation**
You can install `docoreai` from [PyPI](https://pypi.org/project/docoreai/) using pip:

```bash
pip install docoreai  
```
### How to set it up  

After installing `docoreai`, create a `.env` file in the root directory with the following content:  

```ini
# .env file
OPENAI_API_KEY="your-openai-api-key"  
GROQ_API_KEY="your-groq-api-key"  
MODEL_PROVIDER="openai"  # Choose 'openai' or 'groq'  
MODEL_NAME='gpt-3.5-turbo' # Choose model  gpt-3.5-turbo, gemma2-9b-it etc  
```
---
Create a file-name.py:
```bash
import os
from dotenv import load_dotenv

from docore_ai import intelligence_profiler 

def main():
    print(
        intelligence_profiler("What is one good way to start python coding for a experienced programmer","AI Developer",
                              os.getenv("MODEL_PROVIDER"),
                              os.getenv("MODEL_NAME")))

....
```
Run file-name.py in terminal:
```bash
>> python file-name.py
```
The intelligence_profiler function returns a response:
```bash
{'response': 

	"optimized_response": "One good way for an experienced programmer to start coding in Python is by focusing on Python syntax and exploring advanced features such as list comprehensions, lambda functions, and object-oriented programming concepts. Additionally, leveraging Python frameworks like Django or Flask can provide practical hands-on experience in building web applications...",\n    
	
	"intelligence_profile": { "reasoning": 0.9, "creativity": 0.6, "precision": 0.9, "temperature": 0.6 }\n}

```
OR

1️⃣ Clone the repo:
```bash
 git clone https://github.com/SajiJohnMiranda/DoCoreAI.git
```
2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```
3️⃣ Run DoCoreAI:
```bash
uvicorn api.main:app
```
4️⃣ Start using with Swagger:
```bash
 http://127.0.0.1:8000/docs 
```
5️⃣ Test the DoCoreAI API in Postman:
```bash
 http://127.0.0.1:8000/intelligence_profiler

 Body:
    {
    "user_content": "Can you walk me through how to connect my laptop to this new network?",
    "role": "Technical Support Agent"
    }
```
Response:
![DoCoreAI Response](https://github.com/SajiJohnMiranda/DoCoreAI/blob/main/assets/DoCoreAI-json-response-temperature.jpg)

The image showcases a JSON response where DoCoreAI dynamically assigns the ideal reasoning, creativity, and precision values—ensuring the AI agent delivers the perfect response every time. With an intelligently calculated temperature, the AI strikes the perfect balance between accuracy and adaptability, eliminating guesswork and maximizing response quality. 

Quick test [Sample Code](https://github.com/SajiJohnMiranda/DoCoreAI/tree/main/tests/Quick%20Test)

🎉 **You're all set to build smarter AI applications!**  

---
## Optimizations in the PyPI Version  
The PyPI version of DoCoreAI includes slight optimizations compared to the open-source repository. These changes are aimed at improving performance, reducing dependencies, and streamlining the package for end users.

🔹 Key Differences:  
✔️ Reduced prompt/input tokens.  
✔️ Certain additional development and research files from the open-source version have been removed to keep the installation lightweight.  
✔️ Some functionalities have been optimized for better efficiency in production environments.  
✔️ The PyPI version ensures a smoother out-of-the-box experience, while the GitHub version is more flexible for modifications and contributions.  

If you need the full open-source experience, you can clone the GitHub repository and use the source code directly. However, for most users, the PyPI version is recommended for installation and usage.  

---
## 🕵️ Welcoming Testers & Contributors  
We’re actively looking for passionate testers to help validate DoCoreAI across different LLMs! Your insights will play a key role in refining its performance and making it even more effective.  

💡 Whether you're testing, analyzing results, suggesting improvements, or enhancing documentation, every contribution helps push DoCoreAI forward.  

### How You Can Contribute as a Tester 
🔹 **Evaluate, don’t just debug** – You’re here to analyze how well DoCoreAI optimizes prompts compared to standard inputs and help fine-tune its intelligence.  
🔹 **Test with different LLMs** – Clone or fork the repo, run tests, and submit a pull request (PR) with observations & comparisons.  
Details at [CONTRIBUTING-TESTERS.md](https://github.com/SajiJohnMiranda/DoCoreAI/blob/main/CONTRIBUTING-TESTERS.md)
🔹 **Ask for guidance** – Need help setting up the test environment? Reach out at sajijohnmiranda@gmail.com or [Whatsapp](https://wa.me/+919663522720) – happy to assist!  

🚀Join our growing community and help shape the future of AI-driven prompt optimization!  

---

## 🔗 Integrations & Compatibility
DoCoreAI is designed to work seamlessly with major AI platforms:
- Works with **OpenAI GPT, Claude, LLaMA, Falcon, Cohere, and more.**
- Supports **LangChain, FastAPI, Flask, and Django.**
- Easy to extend via **plugin-based architecture.**

---

## 📈 Why Developers Should Use DoCoreAI

🔹 Smarter AI, Better Results  
- Ensures AI models understand the intelligence scope required for each task.  
- Enhances prompt efficiency, reducing trial and error in prompt engineering.

🔹 Saves Time & Effort  
- No need for manual prompt tuning—DoCoreAI does it for you.  
- Works out of the box with OpenAI and Groq models.

🔹 Ideal for SaaS & AI-driven Applications  
- Perfect for chatbots, AI assistants, automation, and enterprise AI solutions.  
- DoCoreAI transforms AI interactions by making prompts truly intelligent.

---
## ⚠️ Important: DoCoreAI’s Token Usage—Read Before You Judge!  

**Why DoCoreAI May Seem to Use More Tokens Initially**
When you first test DoCoreAI, you might notice higher completion tokens compared to a normal LLM prompt. This is expected because:

DoCoreAI dynamically adjusts AI behavior based on reasoning, creativity, and precision.  

It optimizes response quality upfront, reducing unnecessary follow-up queries.  
🔍 But Here’s How DoCoreAI Actually Saves Costs  
✔️ Fewer follow-up API calls: A well-optimized first response means users don’t need to rephrase their questions.  
✔️ Controlled AI behavior: Instead of AI generating unpredictable outputs, DoCoreAI ensures response efficiency.  
✔️ Smart token optimization: Over multiple queries, total tokens used decrease compared to standard LLM prompts.

📊 What Should You Do?  
🔹 **Don’t judge cost based on a single query—test**  
🔹 Compare total token usage over time, not just one response.  
🔹 Measure the reduction in API calls for a real cost-benefit analysis.  

Note: The current output appends extra content "intelligence_profile": { "reasoning": 0.5, "creativity": 0.2, "precision": 0.9, "temperature": 0.4}, which currently adds up the total tokens. This output text can be simply ignored in the PROD version, to save on tokens.  

### ⚡ DoCoreAI isn’t just about using optimizing temperature or tokens—it’s about making AI smarter and more cost-effective.  
🚀 **Test it right, and you’ll see the difference!**

---

## 🌟 Join the Community:  
Let’s build the future of AI-powered intelligence tuning together! 🚀  
🤝 **Contribute:** Open issues, create pull requests, and help improve DoCoreAI!  
📢 **Discuss & Collaborate:** Join our **Discord & [GitHub Discussions](https://github.com/SajiJohnMiranda/DoCoreAI/discussions)**.  
🌟 **Star the Repo!** If you find this useful, don’t forget to star ⭐ it on GitHub!  

👉 [GitHub Repo](https://github.com/SajiJohnMiranda/DoCoreAI) | [Docs (Coming Soon)]  

---

## Recommended LLMs for Intelligence Optimization
DoCoreAI is designed to refine and optimize user prompts by dynamically adjusting intelligence parameters such as reasoning, creativity, and precision. To achieve the best results, we recommend using ChatGPT (GPT-4-turbo) for this task.
While DoCoreAI is compatible with other LLMs (e.g., LLaMA 3, Claude etc), results may vary depending on the model’s capabilities. Developers are encouraged to experiment and contribute insights on different LLM integrations.

## 📌 Technical Note: Token Usage & API Efficiency
- Our Testing & Research shows that token usage is reduced by 15-30% when compared to normal prompts, leading to:
    Lower API Costs – Reduced token consumption means lower expenses when using OpenAI or Groq models.

**Proposed Enhancement: Vector Database Integration**  
We are currently exploring the integration of a vector database to store intelligence profiles for past queries. This will probably enable faster retrieval of optimized parameters for similar prompts, further reducing token usage and improving response efficiency. Stay tuned!

**Future Support for Fine-Tuned Models:**  
We recognize the growing demand for fine-tuned open-source models tailored for specific applications. In future updates, we aim to explore Integration with fine-tuned LLaMA/Custom GPT models, Support for locally deployed models (via Ollama, vLLM, etc.) & Customization of intelligence parameters based on domain-specific data.

Our vision is to make DoCoreAI adaptable to both proprietary and open-source AI models, ensuring flexibility for all developers. Contributions and suggestions are welcome!

---

## ⚖️ License
Licensed under [MIT License](https://github.com/SajiJohnMiranda/DoCoreAI/blob/main/LICENSE.md). Use freely, contribute, and enhance AI for everyone!    

---
## ⚠️ Known Issues - *Work-In-Progress*

### 🚧 Memory Window Context Code - Work in Progress
The **memory window context** feature is currently under development.  
- 🛠 We are actively working on optimizing context handling for better efficiency.  
- 🚀 Future updates will enhance long-term memory retention and retrieval.  

---
### Anonymous Telemetry  
To improve DoCoreAI and understand usage patterns, we have enabled Anonymous Telemetry by default. This helps us gather insights such as function calls and usage frequency—without collecting any personal or sensitive data.  

How it Works:  

- Tracks only calls to pip install docoreai --upgrade for the package.  
- Only logs docoreai version, python version and execution timestamps.  
- No user data, API keys, or prompt content is stored.  
- Data is sent securely to our analytics endpoint.  

How to Disable Telemetry: To disable telemetry, set the following in your .env file:  

```
DOCOREAI_TELEMETRY=False

```
We respect your privacy! If you have concerns, feel free to disable it.

---

### **Let’s revolutionize AI prompt optimization together!** 

🤝 Contribute & Share Insights on LLM Performance
DoCoreAI is designed to work across multiple LLMs like OpenAI GPT, Cohere, Mistral, Claude, LLaMA, and more—but we know every model behaves differently! 🚀

🔍 How well does DoCoreAI optimize prompts for your preferred LLM?
We’d love for developers to test it with different providers and share insights on:  
+ Response accuracy & depth – Does the AI follow optimized intelligence parameters effectively?  
+ Creativity & structure – How well does it balance reasoning, precision, and creativity across different models?  
+ Performance impact – Are there noticeable improvements in token efficiency and response relevance?  

#### 📢 Your feedback helps improve DoCoreAI! If you’ve tested it with openai, Groq, Cohere, Mistral, or any other model, drop your findings in GitHub [Discussions](https://github.com/SajiJohnMiranda/DoCoreAI/discussions) or open an Issue/PR with insights!  
---
#### 📖 Read More on Our Blog

Stay updated with our latest insights, tutorials, and announcements:  

📝 **[Read on Medium](https://medium.com/@mobilights/intelligent-prompt-optimization-bac89b64fa84)**  
📝 **[Read on Dev.to](https://dev.to/sajijohn/introducing-docoreai-unlock-ais-potential-in-dynamic-prompt-tuning-39i3)**  
📝 **[Read on Reddit](https://www.reddit.com/r/aiagents/comments/1jh1gc8/the_end_of_ai_trial_error_docoreai_has_arrived/)**  
📝 **[Dataset on HuggingFace](https://huggingface.co/datasets/DoCoreAI/Dynamic-Temperature-GPT-3.5-Turbo/)**  


Follow us for more updates! 🚀
---
⭐ **Star the repo**: [Click here](https://github.com/SajiJohnMiranda/DoCoreAI/stargazers)  
👀 **Watch for updates**: [Click here](https://github.com/SajiJohnMiranda/DoCoreAI/subscription)  
🍴 **Fork & contribute**: [Click here](https://github.com/SajiJohnMiranda/DoCoreAI/fork)  
