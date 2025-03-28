from Data_analysis import *

def main():
    #datasets = ['HumanEval', 'mbpp', 'leetcode', 'BigCodeBench']
    #models = ['gpt-4o', 'gpt-3.5-turbo', 'llama3.1', 'o3-mini']
    
    data_name = input("Enter the dataset: ")
    model_name = input("Enter the model: ")
    train = input("Is it a train list? (If yes Enter 1 if not Enter 0): ")
    codes=generate_code(data_name=data_name, model_name=model_name, train=int(train))
    if data_name == 'HumanEval' or data_name == 'leetcode' or data_name== 'BigCodeBench':
        testcases=oringinal_test_cases(data_name=data_name)
    else:
        testcases = None
    plot=distribution(data_name=data_name, testcases=testcases, codes=codes)
    return plot

if __name__ == "__main__":
    main()
