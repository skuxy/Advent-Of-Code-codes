//
// Created by skux on 02.12.18..
//

#include "main.h"

int main()
{
    int first_result{0};
    std::ifstream input_file(INPUT_FILE);

    if (input_file.is_open())
    {
        first_result = calculate_checksum(input_file);
    } else
    {
        std::cerr << "No input file, idiot!";
        exit(2);
    }
    input_file.close();

    std::cout << first_result << std::endl;

    return 0;
}