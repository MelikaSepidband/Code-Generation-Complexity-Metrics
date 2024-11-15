from datasets import load_dataset
import os
from openai import OpenAI
client = OpenAI(api_key='API-Key')
#llama 3 login:
#huggingface-cli login
import transformers
import torch

from evaluate import load
code_eval_metric = load("code_eval")
import os
os.environ["HF_ALLOW_CODE_EVAL"] = "1"

def load_data(name):
    if name == 'HumanEval':
        data= load_dataset('openai_humaneval')
    elif name =='mbpp':
        data = load_dataset("mbpp", "sanitized")
    elif name == 'leetcode':
        data = load_dataset("greengerong/leetcode")
    return data

def load_model(name):
    if name == 'gpt4o':
       model = 'gpt4o'
    elif name == "gpt-3.5-turbo":
       model = "gpt-3.5-turbo"
    elif name == "llama3.1":
       model = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    return model   

def generate_code(data, model, train=0):
   codes=[]
   assistant_prompt= "Please complete this Python function."
   if train==0:
    if data == load_dataset('openai_humaneval') or data == load_dataset("mbpp", "sanitized"):
       data2= data['test']
    elif data == load_dataset("greengerong/leetcode"):
       data2 = data['train']
    for i in range(len(data2)):
        user_prompt = data2['prompt'][i]
        if model== 'gpt4o':
                message=[{"role": "assistant", "content": assistant_prompt}, {"role": "user", "content": user_prompt}]
                temperature=0.2
                max_tokens=1000
                frequency_penalty=0.0
                response = client.chat.completions.create(
                model="gpt4o",
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
        elif model == "gpt-3.5-turbo":
                message=[{"role": "assistant", "content": assistant_prompt}, {"role": "user", "content": user_prompt}]
                temperature=0.2
                max_tokens=1000
                frequency_penalty=0.0
                response = client.chat.completions.create(
                model="gpt-3.5-turbo",
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
        elif model == "meta-llama/Meta-Llama-3.1-8B-Instruct":
                pipeline = transformers.pipeline(
                "text-generation",
                model=model,
                model_kwargs={"torch_dtype": torch.bfloat16},
                device_map="auto",
                )
                messages = [
                    {"role": "system", "content": "Please write a Python function for the input asked."},
                    {"role": "user", "content": f"{data2['prompt'][i]}"},
                ]

                outputs = pipeline(
                    messages,
                    max_new_tokens=1000,
                    num_return_sequences=1,
                    do_sample=True,
                    temperature=0.2
                )
                a= outputs[0]["generated_text"][-1]['content']
                try:
                    code_block=re.search(r"```python(.*?)```", a, re.DOTALL).group(1).strip()
                except:
                    code_block=a

   elif train ==1: # just when data is mbpp
    data2 = data['train']
    for i in range(len(data2)):
        user_prompt = data2['prompt'][i]
        if model== 'gpt4o':
                message=[{"role": "assistant", "content": assistant_prompt}, {"role": "user", "content": user_prompt}]
                temperature=0.2
                max_tokens=1000
                frequency_penalty=0.0
                response = client.chat.completions.create(
                model="gpt4o",
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
        elif model == "gpt-3.5-turbo":
                message=[{"role": "assistant", "content": assistant_prompt}, {"role": "user", "content": user_prompt}]
                temperature=0.2
                max_tokens=1000
                frequency_penalty=0.0
                response = client.chat.completions.create(
                model="gpt-3.5-turbo",
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
        elif model == "meta-llama/Meta-Llama-3.1-8B-Instruct":
                pipeline = transformers.pipeline(
                "text-generation",
                model=model,
                model_kwargs={"torch_dtype": torch.bfloat16},
                device_map="auto",
                )
                messages = [
                    {"role": "system", "content": "Please write a Python function for the input asked."},
                    {"role": "user", "content": f"{data2['prompt'][i]}"},
                ]

                outputs = pipeline(
                    messages,
                    max_new_tokens=1000,
                    num_return_sequences=1,
                    do_sample=True,
                    temperature=0.2
                )
                a= outputs[0]["generated_text"][-1]['content']
                try:
                    code_block=re.search(r"```python(.*?)```", a, re.DOTALL).group(1).strip()
                except:
                    code_block=a
   codes.append(code_block)
   return codes

def generate_test_cases(function_name, context):

    input_sections = re.findall(r"\*\*Input:\*\*(.*?)\*\*Output:\*\*", context, re.DOTALL)
    output_sections = re.findall(r"\*\*Output:\*\*(.*?)\*\*", context, re.DOTALL)

    test_cases = []
    for inputs, output in zip(input_sections, output_sections):
        inputs = inputs.strip()
        output = output.strip()
        test_case = f"assert {function_name}({inputs}) == {output}"
        cleaned_test = test_case.replace("\\", "")
        test_cases.append(cleaned_test)

    return test_cases

def oringinal_test_cases(data):
    final_test_cases = []
    if data == load_dataset('openai_humaneval'):
        for a_test in human_eval['test']:
            method_names = re.findall('def .*\(', a_test['prompt'])
            if len(method_names) == 2:
                method_name = method_names[1]
            else:
                method_name = method_names[0]
            method_name = method_name.replace('def ', '').replace('(', '')
            test = a_test['test'] + '\ncheck(' + method_name + ')'
            final_test_cases.append(test)
    elif data == load_dataset("greengerong/leetcode"):
        for i in range(len(Lcode['train']['content'])):
            example = Lcode['train']['content'][i]

            function_name = "function_name"
            test_case = generate_test_cases(function_name, example)
            final_test_cases.append(test_case)


def evaluation(data, testcases, code):
    accuracy=[]
    if data == load_dataset('openai_humaneval'):
        for j in range(len(data['test'])):
            pass_at_k, results = code_eval_metric.compute(references=[testcases[j]], predictions=[[code[j]]], k=[1])
            p=pass_at_k['pass@1']
            if p == 1:
                accuracy.append(1)
            else:
                accuracy.append(0)
    elif data == load_dataset("mbpp", "sanitized"):
        len_test=len(mbpp['train']['test_list'][j])
        p=0
        for test in mbpp['train']['test_list'][j]:
            pass_at_k, results = code_eval_metric.compute(references=[testcases[j]], predictions=[[code[j]]], k=[1])
            p+=pass_at_k['pass@1']
        if p==len_test:
            accuracy.append(1)
        else:
            accuracy.append(0)
    elif data == load_dataset("greengerong/leetcode"):
        try:
            len_test=len(testcases[j])
            p=0
            for test in testcases[j]:
                pass_at_k, results = code_eval_metric.compute(references=[testcases[j]], predictions=[[code[j]]], k=[1])
                p+=pass_at_k['pass@1']
                if p==len_test:
                    accuracy.append(1)
                else:
                    accuracy.append(0)
        except:
            accuracy.append(0)
    return accuracy    

