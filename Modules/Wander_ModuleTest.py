from WanderDetection.main_display import WanderDetection
# from FightDetection.main import FightDetection
import argparse
import os
import json
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Please check your model")
    # parser.add_argument("--json_seq_path", type=str, default=os.path.join(os.getcwd(),"data","det_aihub_4"), help="sample json file path")
    parser.add_argument("--json_seq_path", type=str, default="/home/godgang/analysis-request/result/test1", help="sample json file path")

    # try:
    opt = parser.parse_known_args()[0]

    
    model = WanderDetection()

    file_list = os.listdir(opt.json_seq_path)
    file_list =[int(x[:-5]) for x in file_list]
    file_list.sort()
    file_list =[str(x)+".json" for x in file_list]
    # print ("file_list: {}".format(file_list))

    for f in file_list:
        t=os.path.join(opt.json_seq_path,f)
        frame_num = f[:-5] # json file name number
        # print(t)
        with open(t) as od_result_file:
            od_result = json.load(od_result_file)
            print(model.analysis_from_json(od_result,frame_num))
            # print(model.analysis_from_json(od_result).frame)

    # except:
    #     # print("")
    #     # parser.print_help()
    #     sys.exit(0)