# Question Explanation Generator with GPT
Last update: 2023/03/09

## 1. Objective
Finish an API to read in a question (including it's options and correct answer). Generate the explanation for the question by using ChatGPT.

## 2. Checkpoints
1. **Background reading**: Search and read materials about:
   1. The mechanism of GPT model
   2. Difference between different versions of GPT model
   3. The proper prompt to generate more efficient response
   4. How people form their prompts
2. **Prompt engineering**: Tryout different prompts for ChatGPT to find the optimal prompt combination for the best result
3. **Pack & Deploy the API**: (Would be done in our next meeting) Pack the whole processing flow as an online API and deploy to our AWS cloud server.

## 3. Files List
* `gpt.py`: 

## 4. Preparation Before Starting
### 4-1. Get API Key
You need to get a OpenAI API Key before you can use Python (or any other programming language) to call ChatGPT or other OpenAI services.

### 4-2. Install `openai` Package For Your Python Environment
In order to call OpenAI service with Python, we must install the official `openai` package in your python environment. 
