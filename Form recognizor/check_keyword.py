import json
import os

def check_in(content: str, filename: str, result: dict) -> dict:
    kw_path = "keywords/"
    kw_files = os.listdir(kw_path)

    for file in kw_files:
        path = os.path.join(kw_path, file)

        with open(path, 'r', encoding='utf-8') as f:
            keywords = json.load(f)
            print(content)
            for key, values in keywords.items():
                for value in values:
                    if value in content:
                        if key not in result:
                            result[key] = [filename]
                        else:
                            result[key].append(filename)
    print(result)

    return result
