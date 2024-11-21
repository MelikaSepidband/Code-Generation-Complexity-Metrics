import pandas as pd
from Complexity_metrics import *
from generate_evaluate import *
def compute_complexity(data_name, testcases, codes):
    complexity2=[]
    vocabulary2=[]
    length2=[]
    difficulty2=[]
    effort2=[]
    time2=[]
    mi2=[]
    for i in range(codes):
        try:
            cc_result, halstead_result, mi_results = analyze_code_complexity(codes[i])
            complexity2.append(cc_result[0].complexity)
            vocabulary2.append(halstead_result.total.vocabulary)
            length2.append(halstead_result.total.length)
            difficulty2.append(halstead_result.total.difficulty)
            effort2.append(halstead_result.total.effort)
            time2.append(halstead_result.total.time)
            mi2.append(mi_results)
        except:
            complexity2.append(0)
            vocabulary2.append(0)
            length2.append(0)
            difficulty2.append(0)
            effort2.append(0)
            time2.append(0)
            mi2.append(0)
    def_false2=[]
    def_none2=[]
    def_true2=[]
    def_and2=[]
    def_as2=[]
    def_assert2=[]
    def_async2=[]
    def_await2=[]
    def_break2=[]
    def_class2=[]
    def_continue2=[]
    def_def2=[]
    def_del2=[]
    def_elif2=[]
    def_else2=[]
    def_except2=[]
    def_finally2=[]
    def_for2=[]
    def_from2=[]
    def_global2=[]
    def_if2=[]
    def_import2=[]
    def_in2=[]
    def_is2=[]
    def_lambda2=[]
    def_nonlocal2=[]
    def_not2=[]
    def_or2=[]
    def_pass2=[]
    def_print2=[]
    def_raise2=[]
    def_return2=[]
    def_try2=[]
    def_while2=[]
    def_with2=[]
    def_yield2=[]
    for i in range(codes):
        keyword_counts=count_keywords(codes[i])
        def_false2.append(keyword_counts['False'])
        def_none2.append(keyword_counts['None'])
        def_true2.append(keyword_counts['True'])
        def_and2.append(keyword_counts['and'])
        def_as2.append(keyword_counts['as'])
        def_assert2.append(keyword_counts['assert'])
        def_async2.append(keyword_counts['async'])
        def_await2.append(keyword_counts['await'])
        def_break2.append(keyword_counts['break'])
        def_class2.append(keyword_counts['class'])
        def_continue2.append(keyword_counts['continue'])
        def_def2.append(keyword_counts['def'])
        def_del2.append(keyword_counts['del'])
        def_elif2.append(keyword_counts['elif'])
        def_else2.append(keyword_counts['else'])
        def_except2.append(keyword_counts['except'])
        def_finally2.append(keyword_counts['finally'])
        def_for2.append(keyword_counts['for'])
        def_from2.append(keyword_counts['from'])
        def_global2.append(keyword_counts['global'])
        def_if2.append(keyword_counts['if'])
        def_import2.append(keyword_counts['import'])
        def_in2.append(keyword_counts['in'])
        def_is2.append(keyword_counts['is'])
        def_lambda2.append(keyword_counts['lambda'])
        def_nonlocal2.append(keyword_counts['nonlocal'])
        def_not2.append(keyword_counts['not'])
        def_or2.append(keyword_counts['or'])
        def_pass2.append(keyword_counts['pass'])
        def_print2.append(keyword_counts['print'])
        def_raise2.append(keyword_counts['raise'])
        def_return2.append(keyword_counts['return'])
        def_try2.append(keyword_counts['try'])
        def_while2.append(keyword_counts['while'])
        def_with2.append(keyword_counts['with'])
        def_yield2.append(keyword_counts['yield'])
    LOC2=[]
    for i in range(codes):
        try:
            LOC2.append(count_lines(codes[i]))
        except:
            print(i)
            LOC2.append(0)
    loops2=[]
    comparisons2=[]
    variables2=[]
    string_literals2=[]
    numeric_literals2=[]
    math_operations2=[]
    Maxnested_blocks2=[]
    unique_words2=[]
    for i in range(codes):
        loops2.append(count_loops(codes[i]))
        comparisons2.append(count_comparisons(codes[i]))
        try:
            variables2.append(count_variables_in_code(codes[i]))
        except:
            print(i)
            variables2.append(0)
        string_literals2.append(count_string_literals(codes[i]))
        numeric_literals2.append(count_numeric_literals(codes[i]))
        math_operations2.append(count_math_operations(codes[i]))
        Maxnested_blocks2.append(max_nested_blocks(codes[i]))
        unique_words2.append(count_unique_words_in_code(codes[i]))
    accuracy = evaluation(data_name, testcases, codes)
    dataaa = {
        'CC': complexity2,
        'vocabulary': vocabulary2,
        'length': length2,
        'difficulty': difficulty2,
        'effort': effort2,
        'time': time2,
        'mi_index': mi2,
        'LOC': LOC2,
        'loops': loops2,
        'comparisons': comparisons2,
        'variables': variables2,
        'string_literals': string_literals2,
        'numeric_literals': numeric_literals2,
        'math_operations': math_operations2,
        'Maxnested_blocks': Maxnested_blocks2,
        'unique_words': unique_words2,
        'false': def_false2,
        'none': def_none2,
        'true': def_true2,
        'and': def_and2,
        'as': def_as2,
        'assert': def_assert2,
        'async': def_async2,
        'await': def_await2,
        'break': def_break2,
        'class': def_class2,
        'continue': def_continue2,
        'def': def_def2,
        'del': def_del2,
        'elif': def_elif2,
        'else': def_else2,
        'except': def_except2,
        'finally': def_finally2,
        'for': def_for2,
        'from': def_from2,
        'global': def_global2,
        'if': def_if2,
        'import': def_import2,
        'in': def_in2,
        'is': def_is2,
        'lambda': def_lambda2,
        'nonlocal': def_nonlocal2,
        'not': def_not2,
        'or': def_or2,
        'pass': def_pass2,
        'print': def_print2,
        'raise': def_raise2,
        'return': def_return2,
        'try': def_try2,
        'while': def_while2,
        'with': def_with2,
        'yield': def_yield2,
        'accuracy': accuracy
    }

    df = pd.DataFrame(dataaa)
    return df

