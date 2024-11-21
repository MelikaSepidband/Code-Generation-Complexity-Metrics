from Feedback_based_method import *
from generate_evaluate import *

def main():
    #datasets = ['HumanEval', 'mbpp', 'leetcode']
    #models = ['gpt4o', 'gpt-3.5-turbo', 'llama3.1']

    data_name = input("Enter the dataset")
    model_name = input("Enter the model")
    test_list = input("Enter the test list(the range in the dataset)")
    iterations = input("Enter the number of iterations")
    final_codes={}
    for i in test_list:
        num, codes= iterative_generation(data_name = data_name,model_name= model_name, num_prompt = i, iterations=iterations)
        final_codes[num]=codes

    if data_name == 'HumanEval':
        acc_all=[]
        final_test_cases= oringinal_test_cases(data_name)
        # iteration 0
        s=0
        for j in test_list:
            pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][0]]], k=[1])
            p=pass_at_k['pass@1']
            s+=p
        acc_all.append(s/len(test_list))
        # iteration 1
        s=0
        for j in test_list:
            try:
                pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][1]]], k=[1])
            except:
                pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][0]]], k=[1])
            p=pass_at_k['pass@1']
            s+=p
        acc_all.append(s/len(test_list))

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
            s+=p
        acc_all.append(s/len(test_list))

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
            s+=p
        acc_all.append(s/len(test_list))

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
            s+=p
        acc_all.append(s/len(test_list))
        # iteration 5
        s=0
        for j in test_list:
            try:
                pass_at_k, results = code_eval_metric.compute(references=[final_test_cases[j]], predictions=[[final_codes[j][5]]], k=[1])
            except:
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
            s+=p
        acc_all.append(s/len(test_list))

        return acc_all
    elif data_name == 'mbpp':
        acc_all=[]
        mbpp=load_data(data_name)
        # iteration 0
        s=0
        for j in test_list:
            len_test=len(mbpp['test']['test_list'][j])
            p=0
            for test in mbpp['test']['test_list'][j]:
                pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][0]]], k=[1])
                p+=pass_at_k['pass@1']
            if p==len_test:
                s+=1
        acc_all.append(s/len(test_list))

        #iteration 1
        s=0
        for j in test_list:
            len_test=len(mbpp['test']['test_list'][j])
            p1=0
            try:
                for test in mbpp['test']['test_list'][j]:
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][1]]], k=[1])
                    p1+=pass_at_k['pass@1']
            except:
                for test in mbpp['test']['test_list'][j]:
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][0]]], k=[1])
                    p1+=pass_at_k['pass@1']
            if p1==len_test:
                s+=1

        acc_all.append(s/len(test_list))

        #iteration 2
        s=0
        for j in test_list:
            len_test=len(mbpp['test']['test_list'][j])
            p1=0
            try:
                for test in mbpp['test']['test_list'][j]:
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][2]]], k=[1])
                    p1+=pass_at_k['pass@1']
            except:
                try:
                    for test in mbpp['test']['test_list'][j]:
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][1]]], k=[1])
                        p1+=pass_at_k['pass@1']
                except:
                    for test in mbpp['test']['test_list'][j]:
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][0]]], k=[1])
                        p1+=pass_at_k['pass@1']
            if p1==len_test:
                s+=1

        acc_all.append(s/len(test_list))

        #iteration 3
        s=0
        for j in test_list:
            len_test=len(mbpp['test']['test_list'][j])
            p1=0
            try:
                for test in mbpp['test']['test_list'][j]:
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][3]]], k=[1])
                    p1+=pass_at_k['pass@1']
            except:
                try:
                    for test in mbpp['test']['test_list'][j]:
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][2]]], k=[1])
                        p1+=pass_at_k['pass@1']
                except:
                    try:
                        for test in mbpp['test']['test_list'][j]:
                            pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][1]]], k=[1])
                            p1+=pass_at_k['pass@1']
                    except:
                        for test in mbpp['test']['test_list'][j]:
                            pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][0]]], k=[1])
                            p1+=pass_at_k['pass@1']
            if p1==len_test:
                s+=1
        acc_all.append(s/len(test_list))

        #iteration 4
        s=0
        for j in test_list:
            len_test=len(mbpp['test']['test_list'][j])
            p1=0
            try:
                for test in mbpp['test']['test_list'][j]:
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][4]]], k=[1])
                    p1+=pass_at_k['pass@1']
            except:
                try:
                    for test in mbpp['test']['test_list'][j]:
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][3]]], k=[1])
                        p1+=pass_at_k['pass@1']
                except:
                    try:
                        for test in mbpp['test']['test_list'][j]:
                            pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][2]]], k=[1])
                            p1+=pass_at_k['pass@1']
                    except:
                        try:
                            for test in mbpp['test']['test_list'][j]:
                                pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][1]]], k=[1])
                                p1+=pass_at_k['pass@1']
                        except:
                            for test in mbpp['test']['test_list'][j]:
                                pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][0]]], k=[1])
                                p1+=pass_at_k['pass@1']
            if p1==len_test:
                s+=1
        acc_all.append(s/len(test_list))

        #iteration 5
        s=0
        for j in test_list:
            len_test=len(mbpp['test']['test_list'][j])
            p1=0
            try:
                for test in mbpp['test']['test_list'][j]:
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][5]]], k=[1])
                    p1+=pass_at_k['pass@1']
            except:
                try:
                    for test in mbpp['test']['test_list'][j]:
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][4]]], k=[1])
                        p1+=pass_at_k['pass@1']
                except:
                    try:
                        for test in mbpp['test']['test_list'][j]:
                            pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][3]]], k=[1])
                            p1+=pass_at_k['pass@1']
                    except:
                        try:
                            for test in mbpp['test']['test_list'][j]:
                                pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][2]]], k=[1])
                                p1+=pass_at_k['pass@1']
                        except:
                            try:
                                for test in mbpp['test']['test_list'][j]:
                                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][1]]], k=[1])
                                    p1+=pass_at_k['pass@1']
                            except:
                                for test in mbpp['test']['test_list'][j]:
                                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[j][0]]], k=[1])
                                    p1+=pass_at_k['pass@1']
            if p1==len_test:
                s+=1
        acc_all.append(s/len(test_list))
    elif data_name == 'leetcode':
        acc_all=[]
        test_cases= oringinal_test_cases(data_name)
        s_all=[0, 3, 6, 7, 10, 14, 15, 17, 21, 28, 32, 33, 34, 39, 40, 41, 44, 52, 53, 55, 56, 57, 59, 61, 63, 66, 68, 69, 71, 76, 77, 83, 88, 95, 114, 117, 118, 119, 120, 121, 122, 125, 126, 127, 133, 134, 135, 136, 145, 151, 152, 153, 154, 158, 161, 163, 164, 166, 168, 169, 171, 172, 173, 176, 177, 181, 182, 185, 188, 192, 195, 197, 198, 200, 202, 207, 208, 209, 213, 216, 217, 222, 223, 227, 228, 231, 235, 237, 243, 247, 250, 251, 259, 262, 267, 270, 271, 272, 278, 279, 283, 286, 287, 290, 291, 293, 294, 295, 296, 299, 300, 302, 305, 306, 310, 321, 323, 326, 328, 329, 331, 332, 334, 335, 336, 337, 338, 340, 342, 343, 345, 346, 347, 353, 354, 356, 358, 359, 361, 362, 363, 364, 365, 367, 370, 373, 377, 378, 379, 380, 381, 383, 384, 388, 389, 390, 392, 395, 396, 397, 400, 403, 404, 406, 415, 417, 418, 419, 423, 424, 425, 429, 430, 431, 435, 436, 437, 438, 443, 444, 445, 446, 448, 449, 458, 459, 460, 461, 463, 464, 468, 476, 477, 479, 480, 481, 485, 487, 488, 492, 497, 498, 499, 500, 503, 505, 506, 509, 513, 519, 520, 521, 522, 527, 533, 535, 536, 539, 540, 541, 544, 545, 547, 549, 550, 551, 552, 553, 554, 556, 562, 564, 565, 566, 570, 573, 574, 577, 578, 581, 582, 584, 585, 586, 588, 591, 592, 593, 594, 595, 596, 600, 601, 606, 608, 610, 611, 618, 620, 623, 624, 626, 627, 634, 635, 639, 642, 644, 645, 647, 649, 653, 655, 656, 657, 659, 660, 662, 663, 664, 665, 667, 668, 672, 673, 678, 680, 681, 687, 688, 689, 692, 694, 697, 699, 703, 709, 714, 720, 730, 737, 775, 789, 794, 796, 798, 799, 803, 804, 819, 844, 849, 850, 860, 868, 882, 923, 930, 944, 945, 946, 964, 981, 998, 999, 1000, 1014, 1017, 1023, 1026, 1028, 1029, 1035, 1037, 1039, 1043, 1044, 1047, 1053, 1058, 1068, 1073, 1077, 1079, 1083, 1086, 1091, 1092, 1093, 1095, 1098, 1104, 1110, 1111, 1112, 1113, 1116, 1119, 1121, 1123, 1150, 1156, 1161, 1163, 1167, 1170, 1183, 1188, 1190, 1208, 1210, 1211, 1214, 1224, 1226, 1227, 1233, 1236, 1239, 1243, 1250, 1260, 1264, 1266, 1267, 1270, 1272, 1274, 1276, 1311, 1313, 1323, 1344, 1347, 1348, 1350, 1372, 1379, 1384, 1404, 1408, 1428, 1439, 1440, 1441, 1442, 1450, 1451, 1452, 1454, 1457, 1458, 1463, 1471, 1472, 1487, 1498, 1500, 1507, 1508, 1513, 1514, 1515, 1525, 1526, 1527, 1558, 1566, 1568, 1579, 1611, 1620, 1621, 1645, 1647, 1648, 1656, 1662, 1669, 1670, 1671, 1672, 1679, 1681, 1683, 1690, 1695, 1721, 1728, 1729, 1746, 1747, 1778, 1788, 1789, 1790, 1793, 1804, 1807, 1826, 1834, 1847, 1854, 1858, 1861, 1868, 1888, 1896, 1939, 1945, 1997, 2000, 2011, 2022, 2041, 2044, 2062, 2068, 2078, 2097, 2101, 2102, 2107, 2108, 2112, 2115, 2117, 2120, 2121, 2122, 2129, 2143, 2144, 2147, 2157, 2158, 2159, 2160, 2161, 2163, 2166, 2167, 2170, 2171, 2175, 2177, 2178, 2179, 2180, 2181, 2184, 2185, 2186, 2189, 2192, 2194, 2195, 2201, 2204, 2207, 2208, 2209, 2213, 2218, 2222, 2225, 2227, 2232, 2233, 2247, 2252, 2253, 2255, 2261, 2268, 2273, 2274, 2278, 2283, 2284, 2288, 2292, 2293, 2297, 2301, 2310, 2311, 2316, 2317, 2322, 2326, 2327, 2329, 2331, 2332, 2337, 2339, 2347, 2349, 2352, 2353]

        # iteration 0
        s=0
        for j in test_list:
            len_test=len(test_cases[s_all[j]])
            p=0
            for test in test_cases[s_all[j]]:
                try:
                    f_name=find_first_top_level_function(final_codes[s_all[j]][0])

                    test=test.replace('function_name', f_name)
                except:
                    test=test
                pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][0]]], k=[1])
                p+=pass_at_k['pass@1']
            if p==len_test:
                s+=1
        acc_all.append(s/len(test_list))

        # iteration 1
        s=0
        for j in test_list:
            len_test=len(test_cases[s_all[j]])
            p=0
            try:
                for test in test_cases[s_all[j]]:
                    try:
                        f_name=find_first_top_level_function(final_codes[s_all[j]][1])

                        test=test.replace('function_name', f_name)
                    except:
                        test=test
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][1]]], k=[1])
                    p+=pass_at_k['pass@1']
            except:
                for test in test_cases[s_all[j]]:
                    try:
                        f_name=find_first_top_level_function(final_codes[s_all[j]][0])

                        test=test.replace('function_name', f_name)
                    except:
                        test=test
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][0]]], k=[1])
                    p+=pass_at_k['pass@1']
            if p==len_test:
                s+=1
        acc_all.append(s/len(test_list))

        # iteration 2
        s=0
        for j in test_list:
            len_test=len(test_cases[s_all[j]])
            p=0
            try:
                for test in test_cases[s_all[j]]:
                    try:
                        f_name=find_first_top_level_function(final_codes[s_all[j]][2])

                        test=test.replace('function_name', f_name)
                    except:
                        pass
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][2]]], k=[1])
                    p+=pass_at_k['pass@1']
            except:
                try:
                    for test in test_cases[s_all[j]]:
                        try:
                            f_name=find_first_top_level_function(final_codes[s_all[j]][1])

                            test=test.replace('function_name', f_name)
                        except:
                            pass
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][1]]], k=[1])
                        p+=pass_at_k['pass@1']
                except:
                    for test in test_cases[s_all[j]]:
                        try:
                            f_name=find_first_top_level_function(final_codes[s_all[j]][0])

                            test=test.replace('function_name', f_name)
                        except:
                            pass
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][0]]], k=[1])
                        p+=pass_at_k['pass@1']
            if p==len_test:
                s+=1
        acc_all.append(s/len(test_list))

        # iteration 3
        s=0
        for j in test_list:
            len_test=len(test_cases[s_all[j]])
            p=0
            try:
                for test in test_cases[s_all[j]]:
                    try:
                        f_name=find_first_top_level_function(final_codes[s_all[j]][3])

                        test=test.replace('function_name', f_name)
                    except:
                        pass
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][3]]], k=[1])
                    p+=pass_at_k['pass@1']
            except:
                try:
                    for test in test_cases[s_all[j]]:
                        try:
                            f_name=find_first_top_level_function(final_codes[s_all[j]][2])

                            test=test.replace('function_name', f_name)
                        except:
                            pass
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][2]]], k=[1])
                        p+=pass_at_k['pass@1']
                except:
                    try:
                        for test in test_cases[s_all[j]]:
                            try:
                                f_name=find_first_top_level_function(final_codes[s_all[j]][1])

                                test=test.replace('function_name', f_name)
                            except:
                                pass
                            pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][1]]], k=[1])
                            p+=pass_at_k['pass@1']
                    except:
                        for test in test_cases[s_all[j]]:
                            try:
                                f_name=find_first_top_level_function(final_codes[s_all[j]][0])

                                test=test.replace('function_name', f_name)
                            except:
                                pass
                            pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][0]]], k=[1])
                            p+=pass_at_k['pass@1']
            if p==len_test:
                s+=1

        acc_all.append(s/len(test_list))

        # iteration 4
        s=0
        for j in test_list:
            len_test=len(test_cases[s_all[j]])
            p=0
            try:
                for test in test_cases[s_all[j]]:
                    try:
                        f_name=find_first_top_level_function(final_codes[s_all[j]][4])

                        test=test.replace('function_name', f_name)
                    except:
                        pass
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][4]]], k=[1])
                    p+=pass_at_k['pass@1']
            except:
                try:
                    for test in test_cases[s_all[j]]:
                        try:
                            f_name=find_first_top_level_function(final_codes[s_all[j]][3])

                            test=test.replace('function_name', f_name)
                        except:
                            pass
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][3]]], k=[1])
                        p+=pass_at_k['pass@1']
                except:
                    try:
                        for test in test_cases[s_all[j]]:
                            try:
                                f_name=find_first_top_level_function(final_codes[s_all[j]][2])

                                test=test.replace('function_name', f_name)
                            except:
                                pass
                            pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][2]]], k=[1])
                            p+=pass_at_k['pass@1']
                    except:
                        try:
                            for test in test_cases[s_all[j]]:
                                try:
                                    f_name=find_first_top_level_function(final_codes[s_all[j]][1])

                                    test=test.replace('function_name', f_name)
                                except:
                                    pass
                                pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][1]]], k=[1])
                                p+=pass_at_k['pass@1']
                        except:
                            for test in test_cases[s_all[j]]:
                                try:
                                    f_name=find_first_top_level_function(final_codes[s_all[j]][0])

                                    test=test.replace('function_name', f_name)
                                except:
                                    pass
                                pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][0]]], k=[1])
                                p+=pass_at_k['pass@1']
            if p==len_test:
                s+=1

        acc_all.append(s/len(test_list))

        # iteration 5
        s=0
        for j in test_list:
            len_test=len(test_cases[s_all[j]])
            p=0
            try:
                for test in test_cases[s_all[j]]:
                    try:
                        f_name=find_first_top_level_function(final_codes[s_all[j]][5])
                        test=test.replace('function_name', f_name)
                    except:
                        pass
                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][5]]], k=[1])
                    p+=pass_at_k['pass@1']
            except:
                try:
                    for test in test_cases[s_all[j]]:
                        try:
                            f_name=find_first_top_level_function(final_codes[s_all[j]][4])

                            test=test.replace('function_name', f_name)
                        except:
                            pass
                        pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][4]]], k=[1])
                        p+=pass_at_k['pass@1']
                except:
                    try:
                        for test in test_cases[s_all[j]]:
                            try:
                                f_name=find_first_top_level_function(final_codes[s_all[j]][3])

                                test=test.replace('function_name', f_name)
                            except:
                                pass
                            pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][3]]], k=[1])
                            p+=pass_at_k['pass@1']
                    except:
                        try:
                            for test in test_cases[s_all[j]]:
                                try:
                                    f_name=find_first_top_level_function(final_codes[s_all[j]][2])

                                    test=test.replace('function_name', f_name)
                                except:
                                    pass
                                pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][2]]], k=[1])
                                p+=pass_at_k['pass@1']
                        except:
                            try:
                                for test in test_cases[s_all[j]]:
                                    try:
                                        f_name=find_first_top_level_function(final_codes[s_all[j]][1])

                                        test=test.replace('function_name', f_name)
                                    except:
                                        pass
                                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][1]]], k=[1])
                                    p+=pass_at_k['pass@1']
                            except:
                                for test in test_cases[s_all[j]]:
                                    try:
                                        f_name=find_first_top_level_function(final_codes[s_all[j]][0])

                                        test=test.replace('function_name', f_name)
                                    except:
                                        pass
                                    pass_at_k, results = code_eval_metric.compute(references=[test], predictions=[[final_codes[s_all[j]][0]]], k=[1])
                                    p+=pass_at_k['pass@1']
            if p==len_test:
                s+=1

        acc_all.append(s/len(test_list))

if __name__ == "__main__":
    acc_all= main()
    print(acc_all)