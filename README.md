# 현재 동작하지 않아서 도움 필요 KoAlpaca.cpp

Run a fast ChatGPT-like model locally on your device. The screencast below is not sped up and running on an M2 Macbook Air with 4GB of weights. 


[![asciicast](screencast.gif)](https://asciinema.org/a/dfJ8QXZ4u978Ona59LPEldtKK)


This combines the [LLaMA foundation model](https://github.com/facebookresearch/llama) with an [KoAlpaca](https://github.com/Beomi/KoAlpaca) a fine-tuning of the base model to obey instructions (akin to the [RLHF](https://huggingface.co/blog/rlhf) used to train ChatGPT) and a set of modifications to [llama.cpp](https://github.com/ggerganov/llama.cpp) to add a chat interface. 

## Get started cpp
```
# 1. Install required packages:
#    Check if Python 3 is installed: 
python3 --version

#    Install Python 3 if not installed:
#    	Ubuntu: 
sudo apt update && sudo apt install python3 python3-pip python3-venv

#    	macOS: 
brew install python

#     Install required Python packages: 
pip3 install torch transformers onnx


# 2. Clone the repository and change into the repository directory:
git clone https://github.com/gyunggyung/KoAlpaca.cpp
cd KoAlpaca.cpp

# 3. Save the provided Python script in a previous response as convert_to_onnx.py. Replace your-model-name with the name of your model.

# 4. Run the script to convert the model to ONNX format: 
python3 convert_to_onnx.py

# 5. Test the ONNX model using the provided Python script: python3 test_onnx.py
#    This should output the input text and the predicted token.

# 6. Install ONNX Runtime: 
pip3 install onnxruntime

# 7. Compile the C++ code:
g++ main.cpp -o main -lonnxruntime
./main
```

### alpaca.cpp

You can download the weights for `ggml-alpaca-7b-q4.bin` with BitTorrent `magnet:?xt=urn:btih:5aaceaec63b03e51a98f04fd5c42320b2a033010&dn=ggml-alpaca-7b-q4.bin&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce`


Alternatively you can download them with IPFS.

```
# any of these will work
wget -O ggml-alpaca-7b-q4.bin -c https://gateway.estuary.tech/gw/ipfs/QmQ1bf2BTnYxq73MFJWu1B7bQ2UD6qG7D7YDCxhTndVkPC
wget -O ggml-alpaca-7b-q4.bin -c https://ipfs.io/ipfs/QmQ1bf2BTnYxq73MFJWu1B7bQ2UD6qG7D7YDCxhTndVkPC
wget -O ggml-alpaca-7b-q4.bin -c https://cloudflare-ipfs.com/ipfs/QmQ1bf2BTnYxq73MFJWu1B7bQ2UD6qG7D7YDCxhTndVkPC
```

Save the `ggml-alpaca-7b-q4.bin` file in the same directory as your `./chat` executable. 

The weights are based on the published fine-tunes from `alpaca-lora`, converted back into a pytorch checkpoint with a [modified script](https://github.com/tloen/alpaca-lora/pull/19) and then quantized with llama.cpp the regular way. 


## Get started python
To chat with the KoAlpaca model using the provided Python script, simply follow these steps:
1. Install Python 3 and the necessary dependencies (Hugging Face Transformers and PyTorch libraries).
2. Save the koalpaca.py script in a directory of your choice.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script by entering python3 koalpaca.py.
5. Type your input message and press Enter to see the model's generated response.
6. Continue chatting by entering more messages, and type 'quit' when you wish to exit the chat.

### Ubuntu

```
git clone https://github.com/gyunggyung/KoAlpaca.cpp
cd KoAlpaca.cpp

pip3 install --user transformers
pip3 install --user torch

python3 koalpaca.py
```

### macOS
```
git clone https://github.com/gyunggyung/KoAlpaca.cpp

cd /Users/YourUsername/koalpaca

pip3 install --user transformers
pip3 install --user torch

python3 koalpaca.py
```

### Windows
```
git clone https://github.com/gyunggyung/KoAlpaca.cpp

cd C:\koalpaca

pip install transformers
pip install torch

python koalpaca.py
```


## Old
```
git clone https://github.com/gyunggyung/KoAlpaca.cpp
cd KoAlpaca.cpp

g++ -o koalpaca koalpaca.cpp -I/path/to/transformers/include -L/path/to/transformers/lib -ltransformers -lonnx -ltorch -lc10
./koalpaca

make chat
./chat
```


### Completed models: Korean model (Polyglot-ko) & English model (LLAMA)

KoAlpaca used two models as backbone models.

1. based on Polyglot-ko 5.8B -> [https://huggingface.co/beomi/KoAlpaca-Polyglot](https://huggingface.co/beomi/KoAlpaca-Polyglot)
2. based on Meta LLAMA 7B -> [https://huggingface.co/beomi/KoAlpaca](https://huggingface.co/beomi/KoAlpaca)

Meta's LLAMA model does not train enough Korean datasets, so there is an issue with low Korean performance when running the actual inference.

To get better quality for Korean, we trained two models using Polyglot-ko 5.8B as a backbone.


## Credit

First of all, I am very grateful to [KoAlpaca: Korean Alpaca Model based on Stanford Alpaca (feat. LLAMA and Polyglot-ko)](https://github.com/Beomi/KoAlpaca). Most of all, thank you [@Beomi](https://github.com/Beomi) for giving me the best choice to make a Korean model.

This combines [Facebook's LLaMA](https://github.com/facebookresearch/llama), [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html), [alpaca-lora](https://github.com/tloen/alpaca-lora) and [corresponding weights](https://huggingface.co/tloen/alpaca-lora-7b/tree/main) by Eric Wang (which uses [Jason Phang's implementation of LLaMA](https://github.com/huggingface/transformers/pull/21955) on top of Hugging Face Transformers), and [llama.cpp](https://github.com/ggerganov/llama.cpp) by Georgi Gerganov. The chat implementation is based on Matvey Soloviev's [Interactive Mode](https://github.com/ggerganov/llama.cpp/pull/61) for llama.cpp. Inspired by [Simon Willison's](https://til.simonwillison.net/llms/llama-7b-m2) getting started guide for LLaMA.


## Disclaimer

Note that the model weights are only to be used for research purposes, as they are derivative of LLaMA, and uses the published instruction data from the Stanford Alpaca project which is generated by OpenAI, which itself disallows the usage of its outputs to train competing models. 


