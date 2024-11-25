import re
from datasets import load_dataset
import os
from openai import OpenAI
api_key = input("Please enter your API Key ")
client = OpenAI(api_key=api_key)
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
    else:
        raise ValueError("Unsupported dataset name")
    return data

def load_model(name):
    if name == 'gpt-4o':
       model = 'gpt-4o'
    elif name == "gpt-3.5-turbo":
       model = "gpt-3.5-turbo"
    elif name == "llama3.1":
       model = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    else:
        raise ValueError("Unsupported model name")
    return model   

def generate_code(data_name, model_name, train=0):
   data= load_data(data_name)
   model= load_model(model_name)
   codes=[]
   assistant_prompt= "Please complete this Python function."
   if train==0:
    if data_name == 'HumanEval' or data_name == 'mbpp':
       data2= data['test']
    elif data_name == 'leetcode':
       data2 = data['train']
    for i in range(len(data2)):
        user_prompt = data2['prompt'][i]
        if model== 'gpt-4o':
            message=[{"role": "assistant", "content": assistant_prompt}, {"role": "user", "content": user_prompt}]
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
                # Ensure you have already authenticated with Hugging Face CLI
                # Run `huggingface-cli login` in your terminal before running this script
                #llama 3 login
                #huggingface-cli login
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
        if model== 'gpt-4o':       
                message=[{"role": "assistant", "content": assistant_prompt}, {"role": "user", "content": user_prompt}]
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
                # Ensure you have already authenticated with Hugging Face CLI
                # Run `huggingface-cli login` in your terminal before running this script
                #llama 3 login
                #huggingface-cli login                
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

def oringinal_test_cases(data_name):
    data= load_data(data_name)
    final_test_cases = []
    if data_name == 'HumanEval':
        for a_test in data['test']:
            method_names = re.findall('def .*\(', a_test['prompt'])
            if len(method_names) == 2:
                method_name = method_names[1]
            else:
                method_name = method_names[0]
            method_name = method_name.replace('def ', '').replace('(', '')
            test = a_test['test'] + '\ncheck(' + method_name + ')'
            final_test_cases.append(test)
    elif data_name == 'leetcode':
        for i in range(len(data['train']['content'])):
            example = data['train']['content'][i]

            function_name = "function_name"
            test_case = generate_test_cases(function_name, example)
            final_test_cases.append(test_case)
    
    return final_test_cases


def evaluation(data_name, testcases, code):
    data= load_data(data_name)
    accuracy=[]
    if data_name == 'HumanEval':
        for j in range(len(data['test'])):
            pass_at_k, results = code_eval_metric.compute(references=[testcases[j]], predictions=[[code[j]]], k=[1])
            p=pass_at_k['pass@1']
            if p == 1:
                accuracy.append(1)
            else:
                accuracy.append(0)
    elif data_name == 'mbpp':
        len_test=len(data['train']['test_list'][j])
        p=0
        for test in data['train']['test_list'][j]:
            pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[code[j]]], k=[1])
            p+=pass_at_k['pass@1']
        if p==len_test:
            accuracy.append(1)
        else:
            accuracy.append(0)
    elif data_name == 'leetcode':
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
