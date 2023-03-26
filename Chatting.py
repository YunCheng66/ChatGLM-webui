from transformers import AutoModel, AutoTokenizer

model_path = "./model/chatglm-6b"

history = []
division = '-'*60
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True)

model = model.half().quantize(4).cuda().eval()

def predict(input):
    global history
    output, history = model.chat(tokenizer, input, history)
    print(history[-1][0] + "\n\n" + history[-1][1] + "\n\n\n")
    return history

def load_lessons(name):
    with open(name, mode='r', encoding='utf-8') as f:
        lessons = f.read().split('\n')
    return lessons

lesson_list = load_lessons('Lesson.txt')
print(division)

with open('advice.txt', mode='w', encoding='utf8') as f:
    for i in range(1, len(lesson_list)):
        text = f'{lesson_list[i]}  请结合时间为本次校园活动提出建议'
        output, history = model.chat(tokenizer, text, [])
        f.write(f'{output}\n\n{division}\n\n')
        f.flush()
        