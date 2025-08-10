![DoCoreAI Banner](https://raw.githubusercontent.com/SajiJohnMiranda/DoCoreAI/main/assets/DoCoreAI-Github-header-image.jpg)

# DoCoreAI – AI Prompt Optimization Engine (Developer Edition)

**Optimize LLM prompts • Tune temperature • Reduce LLM cost • Maximize OpenAI efficiency**

DoCoreAI offers a streamlined, open‑source toolkit for prompt engineering and GPT optimization. Built for developers, this version includes core APIs and libraries —without SaaS features like dashboards. For the full experience (metrics, dashboards), explore our [website](https://docoreai.com).

---

---
[![🔥 Downloads](https://static.pepy.tech/badge/docoreai)](https://pepy.tech/project/docoreai)   |   ![📦 Latest Version](https://img.shields.io/pypi/v/docoreai)   |   ![🐍 Python Compatibility](https://img.shields.io/pypi/pyversions/docoreai)   |   [![⭐ GitHub Stars](https://img.shields.io/github/stars/sajijohnmiranda/DoCoreAI)](https://github.com/SajiJohnMiranda/DoCoreAI/stargazers)   |   [![🧾 License](https://img.shields.io/badge/license-CC%20BY--NC--ND%204.0-blue)](https://creativecommons.org/licenses/by-nc-nd/4.0/)  |  
[![📊 View Reports](https://img.shields.io/badge/📊_View_Reports-Dashboard_Insights-brightgreen)](https://docoreai.com/pypi-downloads-docoreai-dashboard-insights/)
 
> 📊 **See how much time, tokens & money you're saving with DoCoreAI's live insights dashboard**



---

## 🔬 What is DoCoreAI?  

**DoCoreAI** is a research-first, open-source framework that **optimizes large language model (LLM) responses on the fly** — without retraining, fine-tuning, or prompt engineering.

It dynamically adjusts **reasoning**, **creativity**, **precision**, and **temperature** based on context and user role — so your AI agents respond with intelligence tailored to the task.

 Whether you're building a support assistant, a creative co-pilot, or a data analyst bot — DoCoreAI ensures clear, cost-effective, and context-aware responses every time.

---
## 🧩 DoCoreAI: Developer Edition vs [SaaS Edition](https://docoreai.com)

Understand the difference between the open-source Developer Edition (available on GitHub) and the full-featured SaaS Edition (available at [docoreai.com](https://docoreai.com)).

| Feature / Capability                              | **Developer Edition (GitHub)**                                       | **SaaS Edition (docoreai.com)**                                                                 |
|---------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Temperature Optimization**                      | Demonstrates how temperature tuning works in code                    | Dynamically adjusts temperature between first and second LLM calls to reflect real impact       |
| **Prompt Strategy**                               | Uses *self-reflection prompting* to estimate ideal temperature       | Same approach, but applies the estimated value in a second call for accurate optimization       |
| **Dashboard & Reports**                           | Not included                                                         | Includes dashboard with reports: *Developer Time Saved*, *Token Waste*, *Cost Savings*, etc.    |
| **Target Users**                                  | Developers testing prompt behavior                                   | Teams, product leads, and senior managers improving AI cost and efficiency                      |
| **Prompt Logging**                                | Prompts not saved; used only in memory                               | Same — with an added feature to locally save prompts for developer inspection                   |
| **Role-Based Prompting**                          | ✅ Supported                                                         | ✅ Supported                                                                                      |

> 💡 Both versions share the same base logic but differ in how deeply they optimize and visualize prompt performance.

---

## 🌍 Why DoCoreAI?  

### ❌ The Problem:  
- LLMs respond generically, often missing the nuances of **role-based intelligence**.  
- Manually tuning prompts or fine-tuning models is expensive, inconsistent, and doesn’t scale.  
- Token usage grows unchecked, increasing operational costs.  

### ✅ The DoCoreAI Solution:  
- 🔁 **Dynamic Intelligence Profiling**: Adapts temperature, creativity, reasoning, and precision on-the-fly.  
- 🧠 **Context-Aware Prompt Optimization**: Generates intelligent prompts for specific user roles or goals.  
- 💸 **Token Efficiency**: Reduces bloat, avoids over-generation, and cuts down on API/token costs.  
- 📦 **Plug-and-Play**: Use with OpenAI, Claude, Groq/Gemma, and other LLM providers.  

---
## ✨ Key Features  

- `intelligence_profiler()` – Adjusts generation parameters intelligently per request  
- `token_profiler()` – Audits cost, detects bloat, and suggests savings  
- `DoCoreAI Pulse` – Test runner for benchmarking DoCoreAI against baselines  	
- Support for evaluating with MMLU, HumanEval, and synthetic prompt-response datasets  

---
## 📈 Milestones

- 🧪 10,000+ PyPI downloads within 40 days  
- 🚀 Launched on [Product Hunt](https://www.producthunt.com/posts/docoreai)  
- 🧠 Active experiments: MMLU, HumanEval, Dahoas synthetic comparisons  
- 📝 Reflection Blog: [25 Days of DoCoreAI](https://mobilights.medium.com/25-days-of-docoreai-a-reflection-on-the-journey-so-far-f832c1210996)  

---
## 🔬 DoCoreAI Lab – Research Vision  
DoCoreAI Lab is an independent research initiative focused on **dynamic prompt optimization, LLM evaluation, and token-efficiency in GenAI systems**.

### We believe that:  
- **AI responses can be smarter** when intelligence is dynamically profiled instead of hardcoded via prompts.  
- **Evaluation should be real-time and role-aware**, just like how humans adapt in different contexts.  
- **Token waste is solvable**, and we’re on a mission to show how optimization can lower cost without compromising quality.  

🔍 **Current Focus Areas**  
- Dynamic temperature tuning based on role-context (Precision, Reasoning, Creativity)  
- Cost profiling & token-efficiency evaluation:-> [View Sheet (Work In Progress)](https://docs.google.com/spreadsheets/d/1ZOQswSkXSX5LVGIuV_P85pfn6jm76uM0iG9R6jng3Q0/edit?usp=sharing) 
- Benchmarks (MMLU, HumanEval, Dahoas, etc.) to validate optimization methods  
- Building toward a future product: **[DoCoreAI Pulse](https://github.com/SajiJohnMiranda/DoCoreAI-Pulse)**  

🤝 **We’re open to**  
- Collaborations with researchers, open-source contributors, and companies  
- Exploratory conversations with incubators or AI investors  

📬 Contact: [email](mailto:sajijohnmiranda@gmail.com) | [LinkedIn](https://www.linkedin.com/in/saji-john-979416171/)


## 🗺️ Public Roadmap (Early View)
| Phase | Focus |
|-------|-------|
| ✅ **Q1 2025** | Launched DoCoreAI on PyPI |
| 🔄 **Q2 2025** | Evaluation suite ([DoCoreAI Pulse](https://github.com/SajiJohnMiranda/DoCoreAI-Pulse)), token profiler, role-based tuning |
| 🔜 **Q3 2025** | Launch interactive web dashboard + SaaS preview |
| 📣 Future | Open evaluation leaderboard, plugin ecosystem for agents |



---

## 🚀 A New Era in AI Optimization  
DoCoreAI **redefines AI interactions** by dynamically optimizing reasoning, creativity, and precision—bringing human-like cognitive intelligence to LLMs for smarter, cost-efficient responses.

---

### **DoCoreAI simplified overview:**

![DoCoreAI Before & After Comparison](https://github.com/SajiJohnMiranda/DoCoreAI/blob/main/assets/Before%20After%20Temp%20DocoreAI.png)

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
### New Feature: Token Profiler: Optimize Your AI Prompt Efficiency
The Token Profiler is a vital feature of DoCoreAI designed to analyze and optimize the efficiency of your AI prompts. By evaluating token usage, it helps identify and reduce unnecessary verbosity, leading to cost savings and improved performance.

Key Features:
Token Count Analysis: Calculates the total number of tokens in your prompt to ensure it aligns with model constraints.​  

**Cost Estimation:** Provides an estimated cost per API call based on token usage, aiding in budget management.​  

**Bloat Score Assessment:** Assigns a 'bloat score' to measure prompt verbosity, helping to flag and refine overly verbose prompts.​  

**Optimization Insights:** Highlights potential savings by optimizing prompts, offering actionable recommendations for efficiency.  

How It Works:  
The Token Profiler evaluates your prompt by:​  

1. Counting Tokens: Determines the number of tokens in the input prompt.​
GitHub  

2. Estimating Costs: Calculates the approximate cost associated with the prompt based on token pricing.​  

3. Assessing Bloat Score: Analyzes the prompt's verbosity to assign a bloat score, indicating potential areas for reduction.​  

4. Suggesting Optimizations: Provides insights into possible cost savings through prompt refinement.  

Example Output:
```
{
  "token_count": 67,
  "estimated_cost": "$0.000101",
  "bloat_score": 1.12,
  "bloat_flag": true,
  "estimated_savings_if_optimized": "$0.000030",
  "estimated_savings%_if_optimized": "30%"
}  
```

In this example, the prompt contains 67 tokens with an estimated cost of $0.000101. The bloat score of 1.12 indicates minimal verbosity, suggesting no immediate need for optimization.​

By integrating the Token Profiler into your workflow, you can ensure that your AI prompts are concise, cost-effective, and performance-optimized.  



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
🤝 How to Collaborate
DoCoreAI is an open research initiative. If you're:

- A researcher or developer interested in LLM evaluation  
- A startup building GenAI tools  
- An investor supporting open research  

📬 Let’s connect → [LinkedIn](https://www.linkedin.com/in/saji-john-979416171/) | [GitHub Issues](https://github.com/SajiJohnMiranda/DoCoreAI/discussions)

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
DoCoreAI is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).
This license **allows personal and academic use only**. Commercial use, modification, or redistribution **requires prior permission**.
📩 For business or licensing inquiries: / Partnerships or Implementation support, contact: **sajijohnmiranda@gmail.com**.

---

## 📜 License Overview

| Usage Type             | Allowed Under CC BY-NC-ND 4.0? |
|------------------------|-------------------------------|
| 🧪 Personal or Academic Use | ✅ Yes                      |
| 🔄 Modify or Derivative Works | ❌ No                    |
| 💼 Commercial Use or SaaS Integration | ❌ Not Allowed Without License |
| 🚀 Internal Business Prototyping | ⚠️ Contact for Evaluation License |
| 📝 Redistribution        | ❌ No                        |

---
## ⚠️ Known Lacking Features - *Work-In-Progress*

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
⭐ **Star the repo**: [Click here](https://github.com/SajiJohnMiranda/DoCoreAI/)  
👀 **Watch for updates**: [Click here](https://github.com/SajiJohnMiranda/DoCoreAI/subscription)  
🍴 **Fork & contribute**: [Click here](https://github.com/SajiJohnMiranda/DoCoreAI/)  
