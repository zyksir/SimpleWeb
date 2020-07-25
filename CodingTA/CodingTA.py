import sys
sys.path.append("/Users/yikaizhu/github/SimpleWeb/CodingTA/")
from basic_framework.repair import BlockRepair
from basic_framework.core_testing import Tester


class CodingTA:
    def __init__(self):
        print("start to init Coding TA")
        self.ques_dir_path = "/Users/yikaizhu/github/SimpleWeb/data/question_4"
        self.tester = Tester(self.ques_dir_path)
        self.br = BlockRepair(self.ques_dir_path, is_offline_ref=False, is_online_ref=True,
                              is_mutation=True, sr_list=[100], exp_time=1)

    def repairCode(self, buggy_code, timeout=60):
        with open("/Users/yikaizhu/github/SimpleWeb/data/question_4/code/wrong/buggy_code.py", "w") as fw:
            fw.write(buggy_code)
        perf_map = self.br.repairOneCode(buggy_code, timeout=timeout)
        return perf_map[100][0]["buggy_code.py"]

if __name__ == '__main__':
    buggy_code = """
def sort_age(lst):
    result = []
    while lst !=[]:
        lowest = lst[0][1]
        index = 0
        for i in range(1,len(lst)):
            if lst[i][1]<lowest:
                index = i
                lowest = lst[i][1]
        result = result +[lst[index]]
        lst.pop[index]
    return result
        
"""
    x = CodingTA()
    perf_map = x.repairCode(buggy_code)
    for key, value in perf_map.items():
        print(" \n \n %s : \n %s" % (key, value))