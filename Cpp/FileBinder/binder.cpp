#include <iostream>
#include <fstream>
#include <vector>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " output_file input_file1 input_file2 ..." << std::endl;
        return 1;
    }

    std::ofstream output_file(argv[1], std::ios::out | std::ios::binary);
    if (!output_file) {
        std::cerr << "Error opening output file: " << argv[1] << std::endl;
        return 1;
    }

    for (int i = 2; i < argc; ++i) {
        std::ifstream input_file(argv[i], std::ios::in | std::ios::binary);
        if (!input_file) {
            std::cerr << "Error opening input file: " << argv[i] << std::endl;
            return 1;
        }

        output_file << input_file.rdbuf();
        input_file.close();
    }

    output_file.close();
    std::cout << "Files concatenated successfully into " << argv[1] << std::endl;

    return 0;
}

