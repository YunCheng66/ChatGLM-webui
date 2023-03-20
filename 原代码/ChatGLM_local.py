from transformers import AutoModel, AutoTokenizer

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
while True:
    input_text = input("[Me]:  ")
    if input_text == "clear":
        history.clear()
        print('OK')
    else:
        output, history = model.chat(tokenizer, input_text, history)
        print("[ChatGLM]:  " + history[-1][1] )
