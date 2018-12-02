//
// Created by skux on 02.12.18..
//

#ifndef DAY1_MAIN_H
#define DAY1_MAIN_H

#include <iostream>
#include <fstream>
#include <map>

#include "day2.cpp"

#define INPUT_FILE "input.txt"
#endif //DAY1_MAIN_H

uint32_t calculate_checksum(std::ifstream &input_file);

std::pair<uint8_t, uint8_t> analyze_line(std::string line);

void operator+=(std::pair<uint8_t, uint8_t> &p1, std::pair<uint8_t, uint8_t> p2);