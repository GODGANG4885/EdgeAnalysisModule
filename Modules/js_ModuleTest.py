from FalldownDetection.main import FalldownDetection
#from WanderDetection.main import WanderDetection
# from FightDetection.main import FightDetection
import argparse
import os
import json
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Please check your model")
    parser.add_argument("--json_seq_path", type=str, default=os.path.join(os.getcwd(),"data","tracking"), help="sample json file path")

    # try:
    opt = parser.parse_known_args()[0]

    
    model = FalldownDetection(0)

    file_list = os.listdir(opt.json_seq_path)
    file_list.sort()
    # print ("file_list: {}".format(file_list))
    with open("wander_0625_result.json", "w") as json_file:
        result =[]
        
        
        for f in file_list:
            t=os.path.join(opt.json_seq_path,f)
            frame_num = f[:-5] # json file name number
            print(frame_num)
            with open(t) as od_result_file:
                od_result = json.load(od_result_file)
                result.append(model.analysis_from_json(od_result))
                # print(model.analysis_from_json(od_result).frame)
        json.dump(result, json_file)

    # except:
    #     print("")
    #     parser.print_help()
    #     sys.exit(0)
