from transformers import AutoModel, AutoTokenizer
from os import system
from yunc import couloed_print

model_path = "./model/chatglm-6b"
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True)
model = model.half().quantize(4).cuda().eval()

print('-'*60)
history = []
unsave_history = False
multi_line = False
while True:
    # 获取输入
    if multi_line:
        input_text = ''
        counter = 0
        print(couloed_print.Colored().yellow("[Me]:  "))
        while True:
            try:
                counter += 1
                input_text += input(couloed_print.Colored().blue(f'Line{str(counter).zfill(2)}:  ')) + '\n'
            except EOFError:
                input_text = input_text.strip()
                break
    else:
        input_text = input(couloed_print.Colored().blue("[Me]:  ").strip())

    # 检查命令
    if input_text.lower() == "clear":
        print(couloed_print.Colored().red(f'[System]:  {len(history)} history cleared.'))
        history.clear()
        continue
    elif input_text.lower() == "cls":
        system('cls')
        print(couloed_print.Colored().red(f'[System]:  record cleared.'))
        continue
    elif "mode" in input_text.lower():
        if input_text.lower() == "mode auto-clear":
            unsave_history = not unsave_history
            if unsave_history:
                if_on = 'On'
            else:
                if_on = 'Off'
            print(couloed_print.Colored().yellow(f'[System]:  Auto-clear Mode: {if_on}'))
            continue
        elif input_text.lower() == "mode multi-line":
            multi_line = not multi_line
            if multi_line:
                if_on = 'On'
            else:
                if_on = 'Off'
            print(couloed_print.Colored().yellow(f'[System]:  Multi-line Mode: {if_on}'))
            continue
        else:
            print(couloed_print.Colored().red('[System]:  Unknown Mode.'))
            continue

    # 获取输出
    output = input_text
    if unsave_history:
        output, history = model.chat(tokenizer, input_text, [])
    else:
        output, history = model.chat(tokenizer, input_text, history)
    print(couloed_print.Colored().green("[ChatGLM]:  ") + output)
