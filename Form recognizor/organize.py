import os
import json
import check_keyword as ck

root_path = "data/"
files = os.listdir(root_path)   # 12 files

kw_root_path = "keywords/"
kw_files = os.listdir((kw_root_path))


for kw_file in kw_files:
    kw_path = os.path.join(kw_root_path, kw_file)
    with open(kw_path, 'r', encoding='utf-8') as f:

        result = {}
        keywords = json.load(f)
        for key, values in keywords.items():
            for value in values:

                for file in files:
                    path = root_path + file
                    with open(path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                        for page in data['pages']:
                            for content in page["lines"]:
                                print(content["content"])
                                if value in content:
                                    if key not in result:
                                        result[key] = [file]
                                    else:
                                        result[key].append(file)
                        break   
                                    
                                    
                                # result = ck.check_in(content["content"], file, result)
                    
    break