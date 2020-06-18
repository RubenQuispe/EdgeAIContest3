import json
import os


train_annotations_path = os.path.join("./train_annotations")
train_annotations_files = os.listdir(train_annotations_path)
ans_converted = {}


def check_dict(x):
    res = {}
    if {"Pedestrian", "Car"} <= x.keys():
        res['Pedestrian'] = x['Pedestrian']
        res['Car'] = x['Car']
    return res


def convert_to_ans_json(train_annotation_file):
    file_name = train_annotation_file.replace('./train_annotations/', '').replace('.json', '')
    with open(train_annotation_file) as f:
        train_json = json.load(f)
        filtered_list = [check_dict(x) for x in train_json['sequence']]
        file_name = file_name + ".mp4"
        ans_converted[file_name] = filtered_list


for train_annotation_file in train_annotations_files:
    print("Converting file {}".format(train_annotation_file))
    convert_to_ans_json(train_annotations_path + "/" + train_annotation_file)


ans_file = 'evaluation_code/ans_converted.json'
with open(ans_file, 'w') as outfile:
    print("Dumping output to {}".format(ans_file))
    json.dump(ans_converted, outfile)
