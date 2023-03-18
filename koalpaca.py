import torch
from transformers import GPT2LMHeadModel, PreTrainedTokenizerFast

def main():
    model_name = "beomi/KoAlpaca"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = PreTrainedTokenizerFast.from_pretrained(model_name)

    print("Type 'quit' to exit the chat.")
    while True:
        input_text = input("User: ")
        if input_text.lower() == "quit":
            break

        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
        response = tokenizer.decode(output[0], skip_special_tokens=True)

        print(f"KoAlpaca: {response}")

if __name__ == "__main__":
    main()
