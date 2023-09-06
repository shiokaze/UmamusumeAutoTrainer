from bot.base.user_data import *
import json
import os
import glob

presets_path = "/umamusume/presets"


def read_presets():
    folder = base_path + presets_path
    preset_list = []
    files = glob.glob(os.path.join(folder, '*.json'))
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            preset_list.append(data)
    return preset_list


def write_preset(preset_json: str):
    preset_info = json.loads(preset_json)
    name = preset_info['name']
    write_file(presets_path+"/"+name+".json", preset_json)









