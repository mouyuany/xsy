import json

# 输入和输出文件名
input_filename = 'data/aishell_small/train_small.jsonl'
output_filename = 'data/aishell_small/train.jsonl'

# 读取JSONL文件并逐行处理
with open(input_filename, 'r', encoding='utf-8') as infile, \
     open(output_filename, 'w', encoding='utf-8') as outfile:
    for line in infile:
        # 解析每行的JSON对象
        item = json.loads(line)
        
        # 添加"age": 10
        # item["age"] = 10
        item["event_target"] = "<|Speech|>"
        item["with_or_wo_itn"] = "<|withitn|>"
        item["emo_target"] = "<|NEUTRAL|>"
        # 将修改后的JSON对象转换为JSON字符串，并写入到输出文件
        # 使用json.dumps确保写入的是字符串，然后写入换行符
        outfile.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f'Processed {input_filename} and saved to {output_filename}')