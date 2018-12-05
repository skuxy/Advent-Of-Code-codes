//
// Created by skux on 02.12.18..
//

#include "main.h"

#define INPUT_FILE "input.txt"

void first_and_second_task()
{
    int first_result{0};
    std::ifstream input_file(INPUT_FILE);

    if (input_file.is_open())
    {
        first_result = get_overlapping(input_file);
    } else
    {
        std::cerr << "No input file, idiot!";
        exit(2);
    }
    input_file.close();

    std::cout << first_result << std::endl;
}


int main(int argc, char **argv)
{

  first_and_second_task();

    return 0;
}