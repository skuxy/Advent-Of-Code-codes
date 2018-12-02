#include <iostream>
#include <fstream>

#include "day1.cpp"

int main()
{
    std::ifstream inputFile;
    inputFile.open(INPUT_FILE);

    if (! inputFile)
    {
        std::cerr << "No input file, idiot!";
        exit(2);
    }

    int result = calculateFrequency();

    std::cout << result << std::endl;
    return 0;
}