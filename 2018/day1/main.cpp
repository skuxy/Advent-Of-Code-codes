#include <iostream>
#include <fstream>
#include "day1.cpp"

#define INPUT_FILE "input.txt"

int main()
{
    int first_result{0};
    std::ifstream input_file(INPUT_FILE);
    if (input_file.is_open())
    {
        first_result = calculate_frequency(input_file);
    }
    else
    {
        std::cerr << "No input file, idiot!";
        exit(2);
    }
    input_file.close();


    std::pair<bool, int> second_result{std::make_pair(false, 0)};
    std::set<int> reached_frequencies;

    while (!second_result.first)
    {
        std::ifstream repeatedly_input_file(INPUT_FILE);

        reached_frequencies.insert(0);

        if (repeatedly_input_file.is_open())
        {
            second_result = freq_to_reach_twice(repeatedly_input_file, reached_frequencies, second_result.second);

            if (second_result.first)
            {
                break;
            }
        }
        else
        {
            std::cerr << "No input file, idiot!";
            exit(2);
        }
        repeatedly_input_file.close();
    }

    std::cout << first_result << std::endl;
    std::cout << second_result.second << std::endl;

    return 0;
}