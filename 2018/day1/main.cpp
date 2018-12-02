#include <iostream>
#include <fstream>
#include "day1.cpp"

#define INPUT_FILE "input.txt"

int main()
{
    std::ifstream input_file(INPUT_FILE);

    int result{0};

    if (input_file.is_open())
    {
        // result = calculate_frequency(input_file);
        result = freq_to_reach_twice(input_file);
    }
    else
    {
        std::cerr << "No input file, idiot!";
        exit(2);
    }

    std::cout << result << std::endl;
    input_file.close();

    return 0;
}