# generating test cases
import re
from openai import OpenAI
api_key = input("Please enter your API Key ")
client = OpenAI(api_key=api_key)
def generate_test(data):
    tests=[]
    for i in range(len(data)):
        gpt_assistant_prompt = """Please generate comprehensive test cases for this function. For that use def check(candidate):
        assert candidate(input)==output"""
        gpt_user_prompt = data['test']['prompt'][i]
        gpt_prompt = gpt_assistant_prompt, gpt_user_prompt

        message=[{"role": "assistant", "content": gpt_assistant_prompt}, {"role": "user", "content": gpt_user_prompt}]
        temperature=0.2
        max_tokens=1000
        frequency_penalty=0.0


        response = client.chat.completions.create(
            model="gpt-4o",
            messages = message,
            temperature=temperature,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty
        )
        res=response.choices[0].message.content
        try:
            code_block = re.search(r"```python(.*?)```", res, re.DOTALL).group(1).strip()
        except:
            code_block = res
        tests.append(code_block)
        #print(code_block)
