//
// Created by skux on 02.12.18..
//

#include "main.h"

void first_task()
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
}

void second_task()
{
    std::ifstream input_file(INPUT_FILE);
    std::vector<std::string> list_of_lines{};

    if (input_file.is_open())
    {
        std::string line;
        while(std::getline(input_file, line))
        {
            list_of_lines.push_back(line);
        }
    } else
    {
        std::cerr << "No input file, idiot!";
        exit(2);
    }
    input_file.close();

    auto second_result = get_common_letters(list_of_lines);

    std::cout << second_result << std::endl;
}

int main(int argc, char **argv)
{

    first_task();
    second_task();

    return 0;
}