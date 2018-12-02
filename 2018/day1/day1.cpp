//
// Created by skux on 02.12.18..
//

#include "day1.h"

int calculate_frequency(std::ifstream &input_file);  // task 1

std::pair<bool, int> freq_to_reach_twice(
        std::ifstream &input_file, std::set<int> &reached_frequencies, int last_frequency);  // task 2

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

std::pair<bool, int> freq_to_reach_twice(std::ifstream &input_file, std::set<int> &reached_frequencies,
                                         int last_frequency)
{
    // task 2
    int current_frequency{last_frequency};
    std::string line;

    while ( std::getline(input_file, line))
    {
        int parsed_frequency = std::stoi(line);
        current_frequency += parsed_frequency;
        auto insert_result = reached_frequencies.insert(current_frequency);

        if (! insert_result.second)
        {
            return std::make_pair(true, current_frequency);
        }
    }

    return std::make_pair(false, current_frequency);
}
