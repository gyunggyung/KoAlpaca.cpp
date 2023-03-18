import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_response(model, tokenizer, prompt, max_length=30):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def main():
    model_name = "beomi/KoAlpaca"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    while True:
        prompt = input("Enter your input text (type 'quit' to exit):\n")
        if prompt.strip().lower() == 'quit':
            break

        response = generate_response(model, tokenizer, prompt)
        print(f"Generated text: {response}\n")

if __name__ == "__main__":
    main()
