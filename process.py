import json
import re

def checkKeywords(keywords, prompt, completion):
    checked = False
    for keyword in keywords:
        checked = checked or (keyword in prompt or keyword in completion)
    return checked

file_path = 'data.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

print('Length of Document', len(data))

# Split based on newline

data = data.split('. ')
# Remove redundant spaces
data = [re.sub('\s+', ' ', s) for s in data if s]
# Remove space at the beginning of the string
data = [s[1:] if s[0] == ' ' else s for s in data ]
# Remove strings that are too short
data = [s for s in data if len(s) > 20]

print('Length of List',len(data))

output_file = file_path.replace('.txt', '.jsonl').replace('data', 'dataset')

with open(output_file, 'w') as f:
    for i in range(0, len(data)):
        if i+1 >= len(data):
            break
        prompt = ''
        completion = ''
        str = data[i]
        str = str.split(' ')
        p = int(len(str) / 2)
        for j in str[:p]:
            prompt += j
            prompt += ' '
        for j in str[p:]:
            completion += j
            completion += ' '
        if checkKeywords(['dialog', 'editing', 'model'], prompt, completion):
        # if True:
            json_data = {'prompt': prompt, 'completion': completion}
            json.dump(json_data, f)
            f.write('\n')

