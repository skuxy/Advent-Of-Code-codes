//
// Created by skux on 02.12.18..
//

#include "main.h"


void operator+=(std::pair<uint8_t, uint8_t> &p1, std::pair<uint8_t, uint8_t> p2)
{
    std::pair<uint8_t , uint8_t> resulting_pair = std::make_pair(p1.first + p2.first, p1.second + p2.second);
    p1 = resulting_pair;
}

uint32_t calculate_checksum(std::ifstream &input_file)
{
    std::string line ;

    std::pair<uint8_t, uint8_t> checksum_factors = std::make_pair(0,0);

    while (std::getline(input_file, line))
    {
        auto line_occs = analyze_line(line);
        checksum_factors += line_occs;
    }

    return checksum_factors.first * checksum_factors.second;
}

std::pair<uint8_t, uint8_t> analyze_line(std::string line)
{
    std::pair result = std::make_pair(0, 0);
    std::map<char, uint8_t> letter_occurences;

    for (char &c : line)
    {
        auto line_it = letter_occurences.find(c);
        if (line_it != letter_occurences.end())
        {
            letter_occurences[c]++ ;
        }
        else
        {
            letter_occurences[c] = 1 ;
        }
    }

    for (auto const& [letter, occurences] : letter_occurences)
    {
        // DGAF which one
        if (occurences == 2)
        {
            result.first = 1;
        }
        else if (occurences == 3)
        {
            result.second = 1;
        }

        if ( result.first && result.second)
        {
            // No need to iterate further
            return result;
        }

    }

    return result;
}
