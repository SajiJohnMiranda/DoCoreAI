# 🛠️ Contributing as a Tester#  
Thank you for your interest in testing DoCoreAI! Your feedback is crucial in ensuring DoCoreAI delivers accurate and efficient prompt optimizations across various LLMs.  

## 🚀 What You’ll Be Doing  
✔️ Compare DoCoreAI responses vs. normal LLM responses.  
✔️ Identify strengths, weaknesses, and edge cases in different test scenarios.  
✔️ Suggest tweaks or improvements based on your findings.  
✔️ Share your observations by opening a GitHub issue or submitting a PR.

## 📝 How to Get Started :  
Set up the test environment.  

**Install python on your machine: https://www.python.org/downloads/**  

**Must create API Tokens to execute the prompts**  For eg: type "Groq API key" in google search  

1️⃣ Enter >> '**pip install docoreai**' in terminal  
        - download the test.py from https://github.com/SajiJohnMiranda/DoCoreAI/blob/main/tests/Quick%20Test/test.py  
        - Create a .env file in the root folder. Enter the details as shown..
        
            ```ini
                # .env file
                OPENAI_API_KEY="your-openai-api-key"  
                GROQ_API_KEY="your-groq-api-key"  
                MODEL_PROVIDER="groq"  # Choose 'openai' or 'groq'  
                MODEL_NAME='gemma2-9b-it' # Choose model  gpt-3.5-turbo, gemma2-9b-it etc  
                ```

        - You may change The PROMPT and ROLE as per your test context  
        - Next run the command >> '**python test.py**'  & Start your test  

2️⃣ Run DoCoreAI Response vs. Normal Response from LLMs and compare results.  
3️⃣ Document your insights and submit feedback via:

GitHub Issues (if you found an inconsistency or improvement area)

Pull Requests (if you have suggestions for test cases or documentation)  
4️⃣ Join discussions & engage with the community!  

📩 Need help? Contact sajijohnmiranda@gmail.com or [Whatsapp](https://wa.me/+919663522720) for assistance in setting up your test environment.  

🎯 Your contributions help shape AI’s future! Thank you!  

