import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from pathlib import Path

model_name = "KoAlpaca.cpp"
output_path = "output_model.onnx"

model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

model.eval()

# Get the input text dynamically
input_text = input("Enter input text: ")
input_ids = tokenizer.encode(input_text, return_tensors="pt")

input_names = ["input_ids"]
output_names = ["output_0"]

dynamic_axes = {
    "input_ids": {0: "batch_size", 1: "sequence_length"},
    "output_0": {0: "batch_size", 1: "sequence_length"},
}

torch.onnx.export(
    model,
    input_ids,
    output_path,
    input_names=input_names,
    output_names=output_names,
    dynamic_axes=dynamic_axes,
    opset_version=12,
)
