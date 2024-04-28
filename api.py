from flask import Flask, jsonify, request, json
from llama_cpp import Llama

app = Flask(__name__)

model_path = "./llama2/llama-2-7b-chat.Q2_K.gguf"
SYSTEM_PROMPT = "You are a professional musician. You will be prompted with a list of names of songs and artists. Select a random song from the list and provide a short phrase describing its genre. Select a random song from the list and provide a short phrase describing its musical style. Select a random song from the list and provide a short phrase describing its instrumentation. Do not acknowledge the prompt. Do not repeat the prompt back. Do not ask for further prompts."
MAX_TOKENS = 1000

model = Llama(model_path=model_path)

def get_prompt(user_p, system_p=SYSTEM_PROMPT):
    prompt = f"""<s>[INST] <<SYS>>
            {system_p}
            <</SYS>>
            {user_p} [/INST]"""
    return prompt

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello World'})

@app.route('/gen', methods=['POST'])
def generate():
    try:
        data = json.loads(request.data)
        if 'prompt' in data:
            prompt = get_prompt(data['prompt'])
            #output = model(prompt, max_tokens=MAX_TOKENS, echo=False)
            return jsonify({'message': 'Post test successful'})
            #out_prompt = output['choices'][0]['text'].splitlines()
            #return jsonify(out_prompt[1:] if len(out_prompt) > 1 else out_prompt)
        else:
            return jsonify({"error": "Missing required parameters"}), 400
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)