#include <iostream>
#include <string>
#include "ggml.h"
#include "utils.h"
#include "chat.cpp"

void simpleChat() {
    std::string input;
    std::cout << "Enter your message (type 'quit' to exit):" << std::endl;

    while (true) {
        std::getline(std::cin, input);

        if (input == "quit") {
            break;
        }

        std::cout << "You said: " << input << std::endl;
        std::cout << "Enter your message (type 'quit' to exit):" << std::endl;
    }
}

int main() {
    std::cout << "Starting the chat application..." << std::endl;
    
    simpleChat();
    
    std::cout << "Chat application finished." << std::endl;
    return 0;
}
