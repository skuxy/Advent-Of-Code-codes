//
// Created by skux on 02.12.18..
//

#include "day1.h"

int calculate_frequency(std::ifstream &input_file);  // task 1

int freq_to_reach_twice(std::ifstream &input_file);  // task 2

int calculate_frequency(std::ifstream &input_file)
{
    // task 1
    int current_frequency{0};
    std::string line;

    while ( std::getline(input_file, line) )
    {
        int parsed_frequency = std::stoi(line);
        current_frequency += parsed_frequency;
    }
    return current_frequency;
}

int freq_to_reach_twice(std::ifstream &input_file)
{
    // task 2
    std::set<int> reached_frequencies;
    reached_frequencies.insert(0); // First one

    std::string line;

    while ( std::getline(input_file, line))
    {
        int parsed_frequency = std::stoi(line);
        auto insert_result = reached_frequencies.insert(parsed_frequency);

        if (! insert_result.second)
        {
            return parsed_frequency;
        }
    }

    return 0; // Some fuckery happened
}
