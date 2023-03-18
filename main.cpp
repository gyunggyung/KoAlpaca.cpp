#include <iostream>
#include <string>

#include "ggml.h"
#include "utils.h"
#include <onnxruntime_c_api.h>
#include <onnxruntime_cxx_api.h>
#include <transformers/transformers.h>
#include <transformers/bert/BertModel.h>

void useKoAlpacaModel() {
    using namespace transformers;

    // Load the KoAlpaca model and tokenizer
    auto model = GPT2Model::from_pretrained("beomi/KoAlpaca");
    auto tokenizer = GPT2Tokenizer::from_pretrained("beomi/KoAlpaca");

    // Get user input
    std::string input_text;
    std::cout << "Enter your input text (type 'quit' to exit):" << std::endl;
    std::getline(std::cin, input_text);

    while (input_text != "quit") {
        // Tokenize the input text
        auto tokens = tokenizer.encode(input_text);
        tokens.input_ids.resize(tokens.input_ids.size() + 1);
        tokens.attention_mask.resize(tokens.attention_mask.size() + 1);

        // Generate a response using the model
        auto outputs = model.generate(tokens);

        // Decode the generated tokens and print the result
        auto generated_text = tokenizer.decode(outputs[0]);
        std::cout << "Generated text: " << generated_text << std::endl;

        // Get the next input
        std::cout << "Enter your input text (type 'quit' to exit):" << std::endl;
        std::getline(std::cin, input_text);
    }
}

int main() {
    std::cout << "Starting the KoAlpaca application..." << std::endl;
    
    useKoAlpacaModel();
    
    std::cout << "KoAlpaca application finished." << std::endl;
    return 0;
}