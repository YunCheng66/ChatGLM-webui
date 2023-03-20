from transformers import AutoModel, AutoTokenizer
from os import system

model_path = "./model/chatglm-6b"

history = []
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True)

model = model.half().quantize(4).cuda().eval()

def predict(input):
    global history
    output, history = model.chat(tokenizer, input, history)
    print(history[-1][0] + "\n\n" + history[-1][1] + "\n\n\n")
    return history

print('-'*60)
unsave_history = False
multi_line = False
while True:
    if multi_line:
        input_text = ''
        counter = 0
        print("[Me]:  ")
        while True:
            try:
                counter += 1
                input_text += input(f'Line{str(counter).zfill(2)}:  ') + '\n'
            except EOFError:
                input_text = input_text.strip()
                break
    else:
        input_text = input("[Me]:  ").strip()

    if input_text.lower() == "clear":
        print(f'[System]:  {len(history)} history cleared.')
        history.clear()
        continue
    elif input_text.lower() == "cls":
        system('cls')
        continue
    elif input_text.lower() == "mode auto-clear":
        unsave_history = not unsave_history
        print(f'[System]:  Auto-clear mode: {unsave_history}')
        continue
    elif input_text.lower() == "mode multi-line":
        multi_line = not multi_line
        print(f'[System]:  Multi-line mode: {multi_line}')
        continue

    if unsave_history:
        output, history = model.chat(tokenizer, input_text, [])
        print("[ChatGLM]:  " + output)
    else:
        output, history = model.chat(tokenizer, input_text, history)
        print("[ChatGLM]:  " + output)
