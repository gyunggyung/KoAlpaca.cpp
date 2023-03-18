import onnxruntime as ort
from transformers import GPT2Tokenizer

model_name = "KoAlpaca.cpp"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

session = ort.InferenceSession("output_model.onnx")
input_text = "안녕하세요."

input_ids = tokenizer.encode(input_text, return_tensors="np")
output = session.run(None, {"input_ids": input_ids})

predicted_index = output[0][0, -1, :].argmax(axis=-1).item()
predicted_token = tokenizer.decode([predicted_index])

print("Input:", input_text)
print("Predicted token:", predicted_token)
