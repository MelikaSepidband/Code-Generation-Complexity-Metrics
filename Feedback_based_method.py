import shap
from sklearn.linear_model import LogisticRegression
def important_metrics(train_list, test_list, df):
    df2_train = df.copy()
    df2_test = df.copy()
    for i in range(len(df)):
        if i in test_list:
            df2_train = df2_train.drop([i])
    for i in range(len(df)):
        if i in train_list:
            df2_test = df2_test.drop([i])
    X_train = df2_train.drop('accuracy', axis=1)
    y_train = df2_train['accuracy']
    X_test = df2_test.drop('accuracy', axis=1)
    y_test = df2_test['accuracy']
    model = LogisticRegression(max_iter=10000, penalty='l2')

    model.fit(X_train, y_train)

    explainer = shap.LinearExplainer(model, X_train)
    shap_values = explainer.shap_values(X_test)

    return shap.summary_plot(shap_values, X_test)

#human eval
from he_testcases_5 import get_testcases
tests2= get_testcases()

import re
final_test_cases_generated2 = []
for a in range(164):
    method_names = re.findall('def .*\(', human_eval['test']['prompt'][a])
    if len(method_names) == 2:
        method_name = method_names[1]
    else:
        method_name = method_names[0]
    method_name = method_name.replace('def ', '').replace('(', '')
    test = tests2[a] + '\ncheck(' + method_name + ')'
    final_test_cases_generated2.append(test)

#mbpp

import pickle

# Specify the path to your pickle file
file_path = '/content/mbpp_generated_testcases'

# Open the pickle file in read-binary mode and load its content
with open(file_path, 'rb') as file:
    tests = pickle.load(file)
tests=tests[120:377]

import re

def get_function_names(code):
    """Extract function names and their line numbers from the code."""
    pattern = re.compile(r'^def (.*?)\(', re.MULTILINE)
    return pattern.findall(code)

def find_last_top_level_function(code):
    """Find the name of the last top-level function in the code."""
    # Split the code into lines
    lines = code.splitlines()
    stack = []
    top_level_functions = []

    for i, line in enumerate(lines):
        # Check for function definitions
        match = re.match(r'^def (.*?)\(', line)
        if match:
            func_name = match.group(1)
            # Determine the function's indentation level
            indent_level = len(line) - len(line.lstrip())
            # If the stack is empty, it's a top-level function
            if not stack:
                top_level_functions.append(func_name)
            stack.append((func_name, indent_level))
        # Check for function end
        if line.strip() == "":
            while stack and len(line) <= stack[-1][1]:
                stack.pop()

    if top_level_functions:
        return top_level_functions[-1]  # Last top-level function name

    return None
#leetcode

from leet_testcases import get_testcases
test_cases_generated=get_testcases()
for i in range(len(test_cases_generated)):
  a=test_cases_generated[i].find("```python")
  if a!=-1:
    test_cases_generated[i]=test_cases_generated[i][a+9:]

s_all=[0, 3, 6, 7, 10, 14, 15, 17, 21, 28, 32, 33, 34, 39, 40, 41, 44, 52, 53, 55, 56, 57, 59, 61, 63, 66, 68, 69, 71, 76, 77, 83, 88, 95, 114, 117, 118, 119, 120, 121, 122, 125, 126, 127, 133, 134, 135, 136, 145, 151, 152, 153, 154, 158, 161, 163, 164, 166, 168, 169, 171, 172, 173, 176, 177, 181, 182, 185, 188, 192, 195, 197, 198, 200, 202, 207, 208, 209, 213, 216, 217, 222, 223, 227, 228, 231, 235, 237, 243, 247, 250, 251, 259, 262, 267, 270, 271, 272, 278, 279, 283, 286, 287, 290, 291, 293, 294, 295, 296, 299, 300, 302, 305, 306, 310, 321, 323, 326, 328, 329, 331, 332, 334, 335, 336, 337, 338, 340, 342, 343, 345, 346, 347, 353, 354, 356, 358, 359, 361, 362, 363, 364, 365, 367, 370, 373, 377, 378, 379, 380, 381, 383, 384, 388, 389, 390, 392, 395, 396, 397, 400, 403, 404, 406, 415, 417, 418, 419, 423, 424, 425, 429, 430, 431, 435, 436, 437, 438, 443, 444, 445, 446, 448, 449, 458, 459, 460, 461, 463, 464, 468, 476, 477, 479, 480, 481, 485, 487, 488, 492, 497, 498, 499, 500, 503, 505, 506, 509, 513, 519, 520, 521, 522, 527, 533, 535, 536, 539, 540, 541, 544, 545, 547, 549, 550, 551, 552, 553, 554, 556, 562, 564, 565, 566, 570, 573, 574, 577, 578, 581, 582, 584, 585, 586, 588, 591, 592, 593, 594, 595, 596, 600, 601, 606, 608, 610, 611, 618, 620, 623, 624, 626, 627, 634, 635, 639, 642, 644, 645, 647, 649, 653, 655, 656, 657, 659, 660, 662, 663, 664, 665, 667, 668, 672, 673, 678, 680, 681, 687, 688, 689, 692, 694, 697, 699, 703, 709, 714, 720, 730, 737, 775, 789, 794, 796, 798, 799, 803, 804, 819, 844, 849, 850, 860, 868, 882, 923, 930, 944, 945, 946, 964, 981, 998, 999, 1000, 1014, 1017, 1023, 1026, 1028, 1029, 1035, 1037, 1039, 1043, 1044, 1047, 1053, 1058, 1068, 1073, 1077, 1079, 1083, 1086, 1091, 1092, 1093, 1095, 1098, 1104, 1110, 1111, 1112, 1113, 1116, 1119, 1121, 1123, 1150, 1156, 1161, 1163, 1167, 1170, 1183, 1188, 1190, 1208, 1210, 1211, 1214, 1224, 1226, 1227, 1233, 1236, 1239, 1243, 1250, 1260, 1264, 1266, 1267, 1270, 1272, 1274, 1276, 1311, 1313, 1323, 1344, 1347, 1348, 1350, 1372, 1379, 1384, 1404, 1408, 1428, 1439, 1440, 1441, 1442, 1450, 1451, 1452, 1454, 1457, 1458, 1463, 1471, 1472, 1487, 1498, 1500, 1507, 1508, 1513, 1514, 1515, 1525, 1526, 1527, 1558, 1566, 1568, 1579, 1611, 1620, 1621, 1645, 1647, 1648, 1656, 1662, 1669, 1670, 1671, 1672, 1679, 1681, 1683, 1690, 1695, 1721, 1728, 1729, 1746, 1747, 1778, 1788, 1789, 1790, 1793, 1804, 1807, 1826, 1834, 1847, 1854, 1858, 1861, 1868, 1888, 1896, 1939, 1945, 1997, 2000, 2011, 2022, 2041, 2044, 2062, 2068, 2078, 2097, 2101, 2102, 2107, 2108, 2112, 2115, 2117, 2120, 2121, 2122, 2129, 2143, 2144, 2147, 2157, 2158, 2159, 2160, 2161, 2163, 2166, 2167, 2170, 2171, 2175, 2177, 2178, 2179, 2180, 2181, 2184, 2185, 2186, 2189, 2192, 2194, 2195, 2201, 2204, 2207, 2208, 2209, 2213, 2218, 2222, 2225, 2227, 2232, 2233, 2247, 2252, 2253, 2255, 2261, 2268, 2273, 2274, 2278, 2283, 2284, 2288, 2292, 2293, 2297, 2301, 2310, 2311, 2316, 2317, 2322, 2326, 2327, 2329, 2331, 2332, 2337, 2339, 2347, 2349, 2352, 2353]

texts=[]
for i in range(len(Lcode['train']['content'])):
  exp=Lcode['train']['content'][i].find("**Example 1:**")
  text=Lcode['train']['content'][i][:exp]
  texts.append(text)
for i in s_all:
  a=test_cases_generated[i].find("# Test case 6")
  if a!=-1:
    test_cases_generated[i]=test_cases_generated[i][:a]
  else:
    b=test_cases_generated[i].find("# Test Case 6")
    if b!=-1:
      test_cases_generated[i]=test_cases_generated[i][:b]
    else:
      print(i)
import re

def get_function_names(code):
    """Extract function names and their line numbers from the code."""
    pattern = re.compile(r'^def (.*?)\(', re.MULTILINE)
    return pattern.findall(code)

def find_first_top_level_function(code):
    """Find the name of the last top-level function in the code."""
    # Split the code into lines
    lines = code.splitlines()
    stack = []
    top_level_functions = []

    for i, line in enumerate(lines):
        # Check for function definitions
        match = re.match(r'^def (.*?)\(', line)
        if match:
            func_name = match.group(1)
            # Determine the function's indentation level
            indent_level = len(line) - len(line.lstrip())
            # If the stack is empty, it's a top-level function
            if not stack:
                top_level_functions.append(func_name)
            stack.append((func_name, indent_level))
        # Check for function end
        if line.strip() == "":
            while stack and len(line) <= stack[-1][1]:
                stack.pop()

    if top_level_functions:
        return top_level_functions[0]  # Last top-level function name

    return None
# gpt4o
def generate_code(assistant_prompt, user_prompt):
    gpt_assistant_prompt = assistant_prompt

    gpt_user_prompt = user_prompt
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
    return code_block

#gpt 3.5 turbo
def generate_code(assistant_prompt, user_prompt):
    gpt_assistant_prompt = assistant_prompt

    gpt_user_prompt = user_prompt
    gpt_prompt = gpt_assistant_prompt, gpt_user_prompt

    message=[{"role": "assistant", "content": gpt_assistant_prompt}, {"role": "user", "content": gpt_user_prompt}]
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
    return code_block

# llama

def generate_code(assistant_prompt, user_prompt):
    messages = [
        {"role": "system", "content": assistant_prompt},
        {"role": "user", "content": user_prompt},
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=1000,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.2
    )
    res= outputs[0]["generated_text"][-1]['content']
    try:
      code_block = re.search(r"```python(.*?)```", res, re.DOTALL).group(1).strip()
    except:
      code_block = res
    return code_block

def evaluate_code(num_prompt, code):
  #all_passed=[]
  pass_at_k, results = code_eval_metric.compute(references=[final_test_cases_generated2[num_prompt]], predictions=[[code]], k=[1])
  p=pass_at_k['pass@1']
  if p!=0:
    return p
    #print("passed: ",num_prompt)
    #all_passed.append(num_prompt)

  else:
    try:
      cc_result, halstead_result, mi_results = analyze_code_complexity(code)
      Cyclomatic_Complexity=cc_result[0].complexity
      vocabulary=halstead_result.total.vocabulary
      length=halstead_result.total.length
      difficulty=halstead_result.total.difficulty
      effort=halstead_result.total.effort
      time=halstead_result.total.time
      mi_index=mi_results
    except:
      Cyclomatic_Complexity=0
      vocabulary=0
      length=0
      difficulty=0
      effort=0
      time=0
      mi_index=0

    keyword_counts=count_keywords(code)
    count_false=keyword_counts['False']
    count_none=keyword_counts['None']
    count_true=keyword_counts['True']
    count_and=keyword_counts['and']
    count_as=keyword_counts['as']
    count_assert=keyword_counts['assert']
    count_async=keyword_counts['async']
    count_await=keyword_counts['await']
    count_break=keyword_counts['break']
    count_class=keyword_counts['class']
    count_continue=keyword_counts['continue']
    count_def=keyword_counts['def']
    count_del=keyword_counts['del']
    count_elif=keyword_counts['elif']
    count_else=keyword_counts['else']
    count_except=keyword_counts['except']
    count_finally=keyword_counts['finally']
    count_for=keyword_counts['for']
    count_from=keyword_counts['from']
    count_global=keyword_counts['global']
    count_if=keyword_counts['if']
    count_import=keyword_counts['import']
    count_in=keyword_counts['in']
    count_is=keyword_counts['is']
    count_lambda=keyword_counts['lambda']
    count_nonlocal=keyword_counts['nonlocal']
    count_not=keyword_counts['not']
    count_or=keyword_counts['or']
    count_pass=keyword_counts['pass']
    count_print=keyword_counts['print']
    count_raise=keyword_counts['raise']
    count_return=keyword_counts['return']
    count_try=keyword_counts['try']
    count_while=keyword_counts['while']
    count_with=keyword_counts['with']
    count_yield=keyword_counts['yield']
    try:
      number_of_lines=count_lines(code)
    except:
      number_of_lines=0
    number_of_loops=count_loops(code)
    number_of_comparisons=count_comparisons(code)
    try:
      number_of_variables=count_variables_in_code(code)
    except:
      number_of_variables=0
    number_of_string_literals=count_string_literals(code)
    number_of_numeric_literals=count_numeric_literals(code)
    number_of_math_operations=count_math_operations(code)
    maximum_nested_block=max_nested_blocks(code)
    number_of_unique_words=count_unique_words_in_code(code)

    return {"cyclomatic_complexity": Cyclomatic_Complexity}, {"halstead_vocabulary": vocabulary}, {"halstead_length": length}, {"halstead_effort": effort}, {"halstead_time": time}, {"halstead_difficulty": difficulty}, {"maintainability_index": mi_index}, {"count_false": count_false}, {"count_none": count_none}, {"count_true": count_true}, {"count_and": count_and}, {"count_as": count_as}, {"count_assert": count_assert}, {"count_async": count_async}, {"count_await": count_await}, {"count_break": count_break}, {"count_class": count_class}, {"count_continue": count_continue}, {"count_def": count_def}, {"count_del": count_del}, {"count_elif": count_elif}, {"count_else": count_else}, {"count_except": count_except}, {"count_finally": count_finally}, {"count_for": count_for}, {"count_from": count_from}, {"count_global": count_global}, {"count_if": count_if}, {"count_import": count_import}, {"count_in": count_in}, {"count_is": count_is}, {"count_lambda": count_lambda}, {"count_nonlocal": count_nonlocal}, {"count_not": count_not}, {"count_or": count_or}, {"count_pass": count_pass}, {"count_print": count_print}, {"count_raise": count_raise}, {"count_return": count_return}, {"count_try": count_try}, {"count_while": count_while}, {"count_with": count_with}, {"count_yield": count_yield}, {"number_of_lines": number_of_lines}, {"number_of_loops": number_of_loops}, {"number_of_comparisons": number_of_comparisons}, {"number_of_variables": number_of_variables}, {"number_of_string_literals": number_of_string_literals}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_math_operations": number_of_math_operations}, {"maximum_nested_block": maximum_nested_block}, {"number_of_unique_words": number_of_unique_words}
    #return {"halstead_length": length}, {"halstead_vocabulary": vocabulary}, {"halstead_effort": effort}, {"number_of_lines": number_of_lines}, {"number_of_math_operations": number_of_math_operations}
    #return {"halstead_length": length}, {"halstead_effort": effort}, {"maintainability_index": mi_index}, {"maximum_nested_block": maximum_nested_block}, {"number_of_lines": number_of_lines}
    #return {"halstead_length": length}, {"halstead_effort": effort},  {"halstead_vocabulary": vocabulary}, {"number_of_numeric_literals": number_of_numeric_literals}, {"maintainability_index": mi_index}
    #return {"halstead_length": length}, {"halstead_effort": effort},  {"halstead_vocabulary": vocabulary}, {"number_of_lines": number_of_lines},  {"number_of_comparisons": number_of_comparisons}
    #return {"halstead_length": length}, {"halstead_effort": effort},  {"halstead_vocabulary": vocabulary}, {"number_of_unique_words": number_of_unique_words}, {"maximum_nested_block": maximum_nested_block}
    #return {"maintainability_index": mi_index}, {"number_of_lines": number_of_lines}, {"number_of_math_operations": number_of_math_operations}, {"halstead_effort": effort},  {"halstead_vocabulary": vocabulary}
    #return {"number_of_lines": number_of_lines}, {"maintainability_index": mi_index}, {"maximum_nested_block": maximum_nested_block},{"number_of_variables": number_of_variables}, {"Cyclomatic_Complexity": Cyclomatic_Complexity}
    #return {"halstead_length": length},{"count_if": count_if}, {"maintainability_index": mi_index},{"number_of_lines": number_of_lines}, {"halstead_effort": effort}
    #return {"halstead_vocabulary": vocabulary}, {"halstead_length": length}, {"number_of_lines": number_of_lines}, {"maintainability_index": mi_index}, {"number_of_variables": number_of_variables}
    #return {"number_of_lines": number_of_lines}, {"maintainability_index": mi_index}, {"number_of_math_operations": number_of_math_operations}, {"maximum_nested_block": maximum_nested_block}, {"number_of_string_literals": number_of_string_literals}
    #return {"cyclomatic_complexity": Cyclomatic_Complexity}, {"halstead_vocabulary": vocabulary}, {"halstead_length": length}, {"halstead_effort": effort}, {"halstead_time": time}, {"halstead_difficulty": difficulty}, {"maintainability_index": mi_index}, {"count_as": count_as},{"count_import": count_import}, {"number_of_lines": number_of_lines}, {"number_of_variables": number_of_variables}, {"number_of_string_literals": number_of_string_literals}, {"number_of_numeric_literals": number_of_numeric_literals}, {"maximum_nested_block": maximum_nested_block}, {"number_of_unique_words": number_of_unique_words}
    #return {"number_of_unique_words": number_of_unique_words}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_lines": number_of_lines}, {"number_of_variables": number_of_variables}, {"count_import": count_import}, {"Maximum_nested_block": maximum_nested_block}, {"count_as": count_as}, {"maintainability_index": mi_index}, {"Cyclomatic_Complexity": Cyclomatic_Complexity}, {"number_of_string_literals": number_of_string_literals}
    #return {"number_of_unique_words": number_of_unique_words}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_lines": number_of_lines}, {"number_of_variables": number_of_variables}, {"count_import": count_import}
    #return {"number_of_lines": number_of_lines}, {"number_of_unique_words": number_of_unique_words}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_variables": number_of_variables}, {"maintainability_index": mi_index}
    #return {"number_of_math_operations": number_of_math_operations}, {"number_of_unique_words": number_of_unique_words}, {"halstead_length": length}, {"count_not": count_not}, {"maintainability_index": mi_index}
    #return {"halstead_length": length}, {"number_of_unique_words": number_of_unique_words}, {"count_not": count_not}, {"number_of_numeric_literals": number_of_numeric_literals}, {"count_return": count_return}

def generate_feedback(metrics):
    #feedback = []
    feedback=f"Please ensure that your generated code has different values for the following complexity metrics: {metrics}"

    return feedback

#our method #humaneval
def iterative_generation(num_prompt, iterations=3):
    assistant_prompt= "please complete this Python function"
    user_prompt = human_eval['test']['prompt'][num_prompt]
    #codes=[]
    for _ in range(iterations):
        code = generate_code(assistant_prompt, user_prompt)
        #print("Generated Code:\n", code)

        metrics = evaluate_code(num_prompt,code)
        #print("Code Metrics:\n", metrics)
        if metrics==1:
           print(f"passed in iteration {_}: ",num_prompt)
           #return "pass", num_prompt, code
           #codes.append(code)
           #return num_prompt, codes
           return num_prompt, code
        else:
           feedback = generate_feedback(metrics)
           assistant_prompt = f"The previous generated code is wrong. Please complete the Python function according to the feedback: {feedback}"
           #codes.append(code)
           #assistant_prompt= "please complete this Python function"
    print("not passed: ", num_prompt)
    #return "not_pass", num_prompt, code
    return num_prompt, code
    #return num_prompt, codes

#baseline #human_eval
def iterative_generation(num_prompt, iterations=3):
    assistant_prompt= "please complete this Python function"
    user_prompt = human_eval['test']['prompt'][num_prompt]
    codes=[]
    for _ in range(iterations):
        code = generate_code(assistant_prompt, user_prompt)
        #print("Generated Code:\n", code)

        metrics = evaluate_code(num_prompt,code)
        #print("Code Metrics:\n", metrics)
        if metrics==1:
           print(f"passed in iteration {_}: ",num_prompt)
           #return "pass", num_prompt, code
           codes.append(code)
           return num_prompt, codes
           #return num_prompt, code
        else:
           #feedback = generate_feedback(metrics)
           assistant_prompt = "The previous generated code is wrong. Please complete the Python function."
           codes.append(code)
           #assistant_prompt= "please complete this Python function"
    print("not passed: ", num_prompt)
    #return "not_pass", num_prompt, code
    #return num_prompt, code
    return num_prompt, codes

#final_codes={}
for i in test_list:
  num, code= iterative_generation(i, iterations=6)
  final_codes[num]=code

# iteration 0
s=0
for j in random_list_test:
  pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes4[j][0]]], k=[1])
  p=pass_at_k['pass@1']
  if p==0:
    print(j)
  s+=p

# iteration 1
s=0
for j in test_list:
  try:
    pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][1]]], k=[1])
  except:
    pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][0]]], k=[1])
  p=pass_at_k['pass@1']
  s+=p
  if p==0:
    print(j)
print(s)

# iteration 2
s=0
for j in test_list:
  try:
    pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][2]]], k=[1])
  except:
    try:
      pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][1]]], k=[1])
    except:
      pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][0]]], k=[1])
  p=pass_at_k['pass@1']
  if p==0:
    print(j)
  s+=p
print(s)

# iteration 3
s=0
for j in test_list:
  try:
    pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][3]]], k=[1])
  except:
    try:
      pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][2]]], k=[1])
    except:
      try:
        pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][1]]], k=[1])
      except:
        pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][0]]], k=[1])
  p=pass_at_k['pass@1']
  if p==0:
    print(j)
  s+=p
print(s)

# iteration 4
s=0
for j in test_list:
  try:
    pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][4]]], k=[1])
  except:
    try:
      pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][3]]], k=[1])
    except:
      try:
        pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][2]]], k=[1])
      except:
        try:
          pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][1]]], k=[1])
        except:
          pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][0]]], k=[1])
  p=pass_at_k['pass@1']
  if p==0:
    print(j)
  s+=p
print(s)

# iteration 5
s=0
for j in test_list:
  try:
    pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes2[j][5]]], k=[1])
  except:
    try:
      pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes2[j][4]]], k=[1])
    except:
      try:
        pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes2[j][3]]], k=[1])
      except:
        try:
          pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes2[j][2]]], k=[1])
        except:
          try:
            pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes2[j][1]]], k=[1])
          except:
            pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes2[j][0]]], k=[1])
  p=pass_at_k['pass@1']
  if p==0:
    print(j)
  s+=p
print(s)

#mbpp
def generate_code(assistant_prompt, num_prompt):
    messages = [
      {"role": "system", "content": assistant_prompt},
      {"role": "user", "content": f"{mbpp['test']['prompt'][num_prompt]}"},
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=1000,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.2
    )
    res=outputs[0]["generated_text"][-1]['content']
    try:
      code_block = re.search(r"```python(.*?)```", res, re.DOTALL).group(1).strip()
    except:
      code_block = res
    last_top_level_func = find_last_top_level_function(code_block)
    if last_top_level_func:
        # Find the function name in the test list
        function_name2 = re.search(r"assert (.*?)\(", mbpp['test']['test_list'][num_prompt][0], re.DOTALL).group(1).strip()
        if function_name2 == "math.isclose":
            function_name2 = re.search(r"assert math\.isclose\((\w+)\(", mbpp['test']['test_list'][num_prompt][0], re.DOTALL).group(1).strip()
        elif function_name2 == "set":
            function_name2 = re.search(r"assert set\((\w+)\(", mbpp['test']['test_list'][num_prompt][0], re.DOTALL).group(1).strip()

        code_block = code_block.replace(last_top_level_func, function_name2)
    code_block= f"import math\n{code_block}"
    return code_block

def evaluate_code(num_prompt, code):
  len_test=len(tests[num_prompt])
  if len_test>5:
    len_test=5
  p=0
  for i in range(len_test):
    pass_at_k, results = code_eval_metric.compute(references=[tests[num_prompt][i]], predictions=[[code]], k=[1])
    p+=pass_at_k['pass@1']
  if p==len_test:
  #pass_at_k, results = code_eval_metric.compute(references=[final_test_cases_mbpp[num_prompt]], predictions=[[code]], k=[1])
  #p=pass_at_k['pass@1']
  #if p==1:
    return "yes"

  else:
    try:
      cc_result, halstead_result, mi_results = analyze_code_complexity(code)
      Cyclomatic_Complexity=cc_result[0].complexity
      vocabulary=halstead_result.total.vocabulary
      length=halstead_result.total.length
      difficulty=halstead_result.total.difficulty
      effort=halstead_result.total.effort
      time=halstead_result.total.time
      mi_index=mi_results
    except:
      Cyclomatic_Complexity=0
      vocabulary=0
      length=0
      difficulty=0
      effort=0
      time=0
      mi_index=0

    keyword_counts=count_keywords(code)
    count_false=keyword_counts['False']
    count_none=keyword_counts['None']
    count_true=keyword_counts['True']
    count_and=keyword_counts['and']
    count_as=keyword_counts['as']
    count_assert=keyword_counts['assert']
    count_async=keyword_counts['async']
    count_await=keyword_counts['await']
    count_break=keyword_counts['break']
    count_class=keyword_counts['class']
    count_continue=keyword_counts['continue']
    count_def=keyword_counts['def']
    count_del=keyword_counts['del']
    count_elif=keyword_counts['elif']
    count_else=keyword_counts['else']
    count_except=keyword_counts['except']
    count_finally=keyword_counts['finally']
    count_for=keyword_counts['for']
    count_from=keyword_counts['from']
    count_global=keyword_counts['global']
    count_if=keyword_counts['if']
    count_import=keyword_counts['import']
    count_in=keyword_counts['in']
    count_is=keyword_counts['is']
    count_lambda=keyword_counts['lambda']
    count_nonlocal=keyword_counts['nonlocal']
    count_not=keyword_counts['not']
    count_or=keyword_counts['or']
    count_pass=keyword_counts['pass']
    count_print=keyword_counts['print']
    count_raise=keyword_counts['raise']
    count_return=keyword_counts['return']
    count_try=keyword_counts['try']
    count_while=keyword_counts['while']
    count_with=keyword_counts['with']
    count_yield=keyword_counts['yield']
    try:
      number_of_lines=count_lines(code)
    except:
      number_of_lines=0

    number_of_loops=count_loops(code)
    number_of_comparisons=count_comparisons(code)
    try:
      number_of_variables=count_variables_in_code(code)
    except:
      number_of_variables=0
    number_of_string_literals=count_string_literals(code)
    number_of_numeric_literals=count_numeric_literals(code)
    number_of_math_operations=count_math_operations(code)
    maximum_nested_block=max_nested_blocks(code)
    number_of_unique_words=count_unique_words_in_code(code)

    #return {"cyclomatic_complexity": Cyclomatic_Complexity}, {"halstead_vocabulary": vocabulary}, {"halstead_length": length}, {"halstead_effort": effort}, {"halstead_time": time}, {"halstead_difficulty": difficulty}, {"maintainability_index": mi_index}, {"count_false": count_false}, {"count_none": count_none}, {"count_true": count_true}, {"count_and": count_and}, {"count_as": count_as}, {"count_assert": count_assert}, {"count_async": count_async}, {"count_await": count_await}, {"count_break": count_break}, {"count_class": count_class}, {"count_continue": count_continue}, {"count_def": count_def}, {"count_del": count_del}, {"count_elif": count_elif}, {"count_else": count_else}, {"count_except": count_except}, {"count_finally": count_finally}, {"count_for": count_for}, {"count_from": count_from}, {"count_global": count_global}, {"count_if": count_if}, {"count_import": count_import}, {"count_in": count_in}, {"count_is": count_is}, {"count_lambda": count_lambda}, {"count_nonlocal": count_nonlocal}, {"count_not": count_not}, {"count_or": count_or}, {"count_pass": count_pass}, {"count_print": count_print}, {"count_raise": count_raise}, {"count_return": count_return}, {"count_try": count_try}, {"count_while": count_while}, {"count_with": count_with}, {"count_yield": count_yield}, {"number_of_lines": number_of_lines}, {"number_of_loops": number_of_loops}, {"number_of_comparisons": number_of_comparisons}, {"number_of_variables": number_of_variables}, {"number_of_string_literals": number_of_string_literals}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_math_operations": number_of_math_operations}, {"maximum_nested_block": maximum_nested_block}, {"number_of_unique_words": number_of_unique_words}
    #return {"number_of_lines": number_of_lines}, {"number_of_math_operations": number_of_math_operations}, {"halstead_length": length}, {"halstead_effort": effort}, {"halstead_difficulty": difficulty}
    #return {"halstead_length": length}, {"halstead_vocabulary": vocabulary}, {"halstead_effort": effort}, {"string_literals": number_of_string_literals}, {"numeric_literals": number_of_numeric_literals}
    #return {"halstead_length": length}, {"halstead_effort": effort}, {"halstead_vocabulary": vocabulary}, {"number_of_math_operations": number_of_math_operations}, {"numeric_literals": number_of_numeric_literals}
    #return {"halstead_length": length}, {"halstead_vocabulary": vocabulary}, {"maximum_nested_block": maximum_nested_block}, {"count_in": count_in}, {"count_return": count_return}
    #return {"number_of_unique_words": number_of_unique_words}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_lines": number_of_lines}, {"number_of_variables": number_of_variables}, {"count_import": count_import}, {"Maximum_nested_block": maximum_nested_block}, {"count_as": count_as}, {"maintainability_index": mi_index}, {"Cyclomatic_Complexity": Cyclomatic_Complexity}, {"number_of_string_literals": number_of_string_literals}, {"halstead_time": time}, {"halstead_effort": effort}, {"halstead_length": length}, {"halstead_difficulty": difficulty}, {"halstead_vocabulary": vocabulary}
    #return {"number_of_unique_words": number_of_unique_words}, {"number_of_numeric_literals": number_of_numeric_literals},{"number_of_lines": number_of_lines}, {"number_of_variables": number_of_variables}, {"count_import": count_import}
    #return {"number_of_lines": number_of_lines}, {"number_of_unique_words": number_of_unique_words}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_variables": number_of_variables}, {"maintainability_index": mi_index}
    return {"halstead_length": length}, {"halstead_vocabulary": vocabulary}, {"cyclomatic_complexity": Cyclomatic_Complexity}, {"halstead_difficulty": difficulty}, {"number_of_math_operations": number_of_math_operations}

def generate_feedback(metrics):
    #feedback = []
    feedback=f"Please ensure that your generated code has different values for the following complexity metrics: {metrics}"

    return feedback
'''
def iterative_generation(num_prompt, iterations=3):
    assistant_prompt= "please complete this Python function"
    user_prompt = mbpp['test']['prompt'][num_prompt]
    for _ in range(iterations):
        code = generate_code(assistant_prompt, user_prompt)
        #print("Generated Code:\n", code)

        metrics = evaluate_code(num_prompt,code)
        #print("Code Metrics:\n", metrics)
        if metrics=="yes":
           print(f"passed in iteration {_}: ",num_prompt)
           return "pass", num_prompt, code
        else:
           feedback = generate_feedback(metrics)
           assistant_prompt = f"The previous generated code is wrong. Please complete the Python function according to the feedback: {feedback}"
           #assistant_prompt= "please complete this Python function"
    print("not passed: ", num_prompt)
    return "not_pass", num_prompt, code
'''
'''
def iterative_generation(num_prompt, iterations=3):
    assistant_prompt= "please complete this Python function"
    #user_prompt = mbpp['test']['prompt'][num_prompt]
    codes=[]
    for _ in range(iterations):
        code = generate_code(assistant_prompt, num_prompt)
        #print("Generated Code:\n", code)

        metrics = evaluate_code(num_prompt,code)
        #print("Code Metrics:\n", metrics)
        if metrics=="yes":
           print(f"passed in iteration {_}: ",num_prompt)
           #return "pass", num_prompt, code
           codes.append(code)
           return num_prompt, codes
           #return num_prompt, code
        else:
           feedback = generate_feedback(metrics)
           assistant_prompt = f"The previous generated code is wrong. Please complete the Python function according to the feedback: {feedback}"
           codes.append(code)
           #assistant_prompt= "please complete this Python function"
    print("not passed: ", num_prompt)
    #return "not_pass", num_prompt, code
    #return num_prompt, code
    return num_prompt, codes
'''
def iterative_generation(num_prompt, iterations=3):
    assistant_prompt= "please complete this Python function"
    #user_prompt = mbpp['test']['prompt'][num_prompt]
    codes=[]
    for _ in range(iterations):
        code = generate_code(assistant_prompt, num_prompt)
        #print("Generated Code:\n", code)

        metrics = evaluate_code(num_prompt,code)
        #print("Code Metrics:\n", metrics)
        if metrics=="yes":
           print(f"passed in iteration {_}: ",num_prompt)
           #return "pass", num_prompt, code
           codes.append(code)
           return num_prompt, codes
           #return num_prompt, code
        else:
           #feedback = generate_feedback(metrics)
           assistant_prompt = "Please complete the Python function"
           codes.append(code)
           #assistant_prompt= "please complete this Python function"
    print("not passed: ", num_prompt)
    #return "not_pass", num_prompt, code
    #return num_prompt, code
    return num_prompt, codes


#leetcode

def generate_code(assistant_prompt, user_prompt):
    gpt_assistant_prompt = assistant_prompt

    #gpt_user_prompt = texts[num_prompt]
    gpt_user_prompt = user_prompt
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
    #generated = find_last_top_level_function(code_block)
    #actual = find_last_top_level_function(mbpp_gpt4o[num_prompt])
    #code_block = code_block.replace(generated, actual)
    return code_block
    '''
    messages = [
        {"role": "system", "content": assistant_prompt},
        {"role": "user", "content": user_prompt},
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=1000,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.2
    )
    res= outputs[0]["generated_text"][-1]['content']
    try:
        code_block = re.search(r"```python(.*?)```", res, re.DOTALL).group(1).strip()
    except:
        code_block = res
    return code_block
    '''
def evaluate_code(num_prompt, code):
  '''
  len_test=len(test_cases[num_prompt])
  p=0
  for test in test_cases[num_prompt]:
    try:
      f_name=find_first_top_level_function(code)

      test=test.replace('function_name', f_name)
    except:
      test=test
    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[code]], k=[1])
    p+=pass_at_k['pass@1']
  if p==len_test:
    return 1.0
  '''
  try:
    f_name=find_first_top_level_function(code)
    t_gen=test_cases_generated[num_prompt] + '\ncheck(' + f_name + ')'
  except:
    t_gen=test_cases_generated[num_prompt]
  pass_at_k, results = code_eval_metric.compute(references=[t_gen], predictions=[[code]], k=[1])
  p=pass_at_k['pass@1']
  if p!=0:
  #pass_at_k, results = code_eval_metric.compute(references=[final_test_cases_mbpp[num_prompt]], predictions=[[code]], k=[1])
  #p=pass_at_k['pass@1']
  #if p==1:
    return p

  else:
    try:
      cc_result, halstead_result, mi_results = analyze_code_complexity(code)
      Cyclomatic_Complexity=cc_result[0].complexity
      vocabulary=halstead_result.total.vocabulary
      length=halstead_result.total.length
      difficulty=halstead_result.total.difficulty
      effort=halstead_result.total.effort
      time=halstead_result.total.time
      mi_index=mi_results
    except:
      Cyclomatic_Complexity=0
      vocabulary=0
      length=0
      difficulty=0
      effort=0
      time=0
      mi_index=0

    keyword_counts=count_keywords(code)
    count_false=keyword_counts['False']
    count_none=keyword_counts['None']
    count_true=keyword_counts['True']
    count_and=keyword_counts['and']
    count_as=keyword_counts['as']
    count_assert=keyword_counts['assert']
    count_async=keyword_counts['async']
    count_await=keyword_counts['await']
    count_break=keyword_counts['break']
    count_class=keyword_counts['class']
    count_continue=keyword_counts['continue']
    count_def=keyword_counts['def']
    count_del=keyword_counts['del']
    count_elif=keyword_counts['elif']
    count_else=keyword_counts['else']
    count_except=keyword_counts['except']
    count_finally=keyword_counts['finally']
    count_for=keyword_counts['for']
    count_from=keyword_counts['from']
    count_global=keyword_counts['global']
    count_if=keyword_counts['if']
    count_import=keyword_counts['import']
    count_in=keyword_counts['in']
    count_is=keyword_counts['is']
    count_lambda=keyword_counts['lambda']
    count_nonlocal=keyword_counts['nonlocal']
    count_not=keyword_counts['not']
    count_or=keyword_counts['or']
    count_pass=keyword_counts['pass']
    count_print=keyword_counts['print']
    count_raise=keyword_counts['raise']
    count_return=keyword_counts['return']
    count_try=keyword_counts['try']
    count_while=keyword_counts['while']
    count_with=keyword_counts['with']
    count_yield=keyword_counts['yield']
    try:
      number_of_lines=count_lines(code)
    except:
      number_of_lines=0

    number_of_loops=count_loops(code)
    number_of_comparisons=count_comparisons(code)
    try:
      number_of_variables=count_variables_in_code(code)
    except:
      number_of_variables=0
    number_of_string_literals=count_string_literals(code)
    number_of_numeric_literals=count_numeric_literals(code)
    number_of_math_operations=count_math_operations(code)
    maximum_nested_block=max_nested_blocks(code)
    number_of_unique_words=count_unique_words_in_code(code)

    #return {"cyclomatic_complexity": Cyclomatic_Complexity}, {"halstead_vocabulary": vocabulary}, {"halstead_length": length}, {"halstead_effort": effort}, {"halstead_time": time}, {"halstead_difficulty": difficulty}, {"maintainability_index": mi_index}, {"count_false": count_false}, {"count_none": count_none}, {"count_true": count_true}, {"count_and": count_and}, {"count_as": count_as}, {"count_assert": count_assert}, {"count_async": count_async}, {"count_await": count_await}, {"count_break": count_break}, {"count_class": count_class}, {"count_continue": count_continue}, {"count_def": count_def}, {"count_del": count_del}, {"count_elif": count_elif}, {"count_else": count_else}, {"count_except": count_except}, {"count_finally": count_finally}, {"count_for": count_for}, {"count_from": count_from}, {"count_global": count_global}, {"count_if": count_if}, {"count_import": count_import}, {"count_in": count_in}, {"count_is": count_is}, {"count_lambda": count_lambda}, {"count_nonlocal": count_nonlocal}, {"count_not": count_not}, {"count_or": count_or}, {"count_pass": count_pass}, {"count_print": count_print}, {"count_raise": count_raise}, {"count_return": count_return}, {"count_try": count_try}, {"count_while": count_while}, {"count_with": count_with}, {"count_yield": count_yield}, {"number_of_lines": number_of_lines}, {"number_of_loops": number_of_loops}, {"number_of_comparisons": number_of_comparisons}, {"number_of_variables": number_of_variables}, {"number_of_string_literals": number_of_string_literals}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_math_operations": number_of_math_operations}, {"maximum_nested_block": maximum_nested_block}, {"number_of_unique_words": number_of_unique_words}
    #return {"number_of_lines": number_of_lines}, {"number_of_math_operations": number_of_math_operations}, {"halstead_length": length}, {"halstead_effort": effort}, {"halstead_difficulty": difficulty}
    #return {"halstead_length": length}, {"halstead_vocabulary": vocabulary}, {"halstead_effort": effort}, {"string_literals": number_of_string_literals}, {"numeric_literals": number_of_numeric_literals}
    #return {"halstead_length": length}, {"halstead_effort": effort}, {"number_of_lines": number_of_lines}, {"halstead_difficulty": difficulty}, {"numeric_literals": number_of_numeric_literals}
    #return {"halstead_length": length}, {"halstead_vocabulary": vocabulary}, {"maximum_nested_block": maximum_nested_block}, {"count_in": count_in}, {"count_return": count_return}
    #return {"count_return": count_return}, {"count_def": count_def}, {"count_in": count_in}, {"number_of_string_literals": number_of_string_literals}, {"count_for": count_for}
    #return {"number_of_unique_words": number_of_unique_words}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_lines": number_of_lines}, {"number_of_variables": number_of_variables}, {"count_import": count_import}, {"Maximum_nested_block": maximum_nested_block}, {"count_as": count_as}, {"maintainability_index": mi_index}, {"Cyclomatic_Complexity": Cyclomatic_Complexity}, {"number_of_string_literals": number_of_string_literals}, {"halstead_time": time}, {"halstead_effort": effort}, {"halstead_length": length}, {"halstead_difficulty": difficulty}, {"halstead_vocabulary": vocabulary}
    #return {"number_of_unique_words": number_of_unique_words}, {"number_of_numeric_literals": number_of_numeric_literals},{"number_of_lines": number_of_lines}, {"number_of_variables": number_of_variables}, {"count_import": count_import}
    #return {"number_of_lines": number_of_lines}, {"number_of_unique_words": number_of_unique_words}, {"number_of_numeric_literals": number_of_numeric_literals}, {"number_of_variables": number_of_variables}, {"maintainability_index": mi_index}
    #return {"halstead_length": length}, {"halstead_vocabulary": vocabulary}, {"count_in": count_in}, {"count_for": count_for}, {"count_class": count_class}
    #return {"count_def": count_def}, {"count_class": count_class}, {"number_of_math_operations": number_of_math_operations}, {"halstead_length": length}, {"number_of_lines": number_of_lines}
    #return {"count_class": count_class}, {"number_of_lines": number_of_lines}, {"halstead_length": length}, {"count_def": count_def}, {"number_of_math_operations": number_of_math_operations}
    #return {"count_def": count_def}, {"halstead_vocabulary": vocabulary}, {"halstead_length": length}, {"number_of_loops": number_of_loops}, {"number_of_unique_words": number_of_unique_words}
    return {"halstead_vocabulary": vocabulary}, {"halstead_length": length}, {"count_def": count_def}, {"count_in": count_in}, {"number_of_loops": number_of_loops}

def generate_feedback(metrics):
    #feedback = []
    feedback=f"Please ensure that your generated code has different values for the following complexity metrics: {metrics}"

    return feedback
'''
def iterative_generation(num_prompt, iterations=3):
    assistant_prompt= "please complete this Python function"
    user_prompt = mbpp['test']['prompt'][num_prompt]
    for _ in range(iterations):
        code = generate_code(assistant_prompt, user_prompt)
        #print("Generated Code:\n", code)

        metrics = evaluate_code(num_prompt,code)
        #print("Code Metrics:\n", metrics)
        if metrics=="yes":
           print(f"passed in iteration {_}: ",num_prompt)
           return "pass", num_prompt, code
        else:
           feedback = generate_feedback(metrics)
           assistant_prompt = f"The previous generated code is wrong. Please complete the Python function according to the feedback: {feedback}"
           #assistant_prompt= "please complete this Python function"
    print("not passed: ", num_prompt)
    return "not_pass", num_prompt, code
'''
def iterative_generation(num_prompt, iterations=3):
    assistant_prompt= "Create a solution in python for the input asked."
    user_prompt = texts[s_all[num_prompt]]
    codes=[]
    for _ in range(iterations):
        code = generate_code(assistant_prompt, user_prompt)
        #print("Generated Code:\n", code)

        metrics = evaluate_code(s_all[num_prompt],code)
        #print("Code Metrics:\n", metrics)
        if metrics==1:
           print(f"passed in iteration {_}: ",s_all[num_prompt])
           #return "pass", num_prompt, code
           codes.append(code)
           return s_all[num_prompt], codes
           #return num_prompt, code
        else:
           feedback = generate_feedback(metrics)
           assistant_prompt = f"The previous generated code is wrong. Create a solution in python for the input asked according to the feedback: {feedback}"
           codes.append(code)
           #assistant_prompt= "please complete this Python function"
    print("not passed: ", s_all[num_prompt])
    #return "not_pass", num_prompt, code
    #return num_prompt, code
    return s_all[num_prompt], codes
def iterative_generation(num_prompt, iterations=3):
    assistant_prompt= "Create a solution in python for the input asked."
    user_prompt = texts[s_all[num_prompt]]
    codes=[]
    for _ in range(iterations):
        code = generate_code(assistant_prompt, user_prompt)
        #print("Generated Code:\n", code)

        metrics = evaluate_code(s_all[num_prompt],code)
        #print("Code Metrics:\n", metrics)
        if metrics==1:
           print(f"passed in iteration {_}: ",s_all[num_prompt])
           #return "pass", num_prompt, code
           codes.append(code)
           return s_all[num_prompt], codes
           #return num_prompt, code
        else:
           #feedback = generate_feedback(metrics)
           assistant_prompt = "Create a solution in python for the input asked."
           codes.append(code)
           #assistant_prompt= "please complete this Python function"
    print("not passed: ", s_all[num_prompt])
    #return "not_pass", num_prompt, code
    #return num_prompt, code
    return s_all[num_prompt], codes