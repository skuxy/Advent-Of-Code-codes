//
// Created by skux on 02.12.18..
//

#include <vector>
#include "main.h"


int get_overlapping(std::ifstream &ifstream);

class Fabric;

void parse_line(Fabric &fabric, std::string line);

class Rectangle
{
public:
    Rectangle(std::string coordinates_str, std::string size_str)
    {
        std::string delimiter{","};
        short idx = coordinates_str.find(delimiter);
        int x_coord = stoi(coordinates_str.substr(0, idx));
        int y_coord = stoi(coordinates_str.substr(idx + 1,  coordinates_str.length()));


        delimiter = "x";
        idx = size_str.find(delimiter);
        int x_size = stoi(size_str.substr(0, idx));
        int y_size = stoi(size_str.substr(idx + 1, size_str.length()));

        this->coordinates = std::make_pair(x_coord, y_coord);
        this->size = std::make_pair(x_size, y_size);
    }

    std::pair<int, int> coordinates;
    std::pair<int, int> size;
};

class Fabric
{
public:
    std::vector<std::vector<int>> fabric;

    std::vector<Rectangle> claims;
public:
    Fabric()
    {
        // can this be done any better?
        std::vector<std::vector<int>> square_fabric(1000, std::vector<int>(1000, 0));
        this->fabric = square_fabric;
    }

    void add_rectangle(Rectangle new_rectangle)
    {
        this->claims.push_back(new_rectangle);

        for(int y = new_rectangle.coordinates.second ; y < new_rectangle.coordinates.second + new_rectangle.size.second; y ++)
        {
            for(int x = new_rectangle.coordinates.first ; x < new_rectangle.coordinates.first + new_rectangle.size.first; x ++ )
            {
                this->fabric[y][x] ++ ;
            }
        }
    }
};

int get_single_claim(Fabric fabric)
{
    for (int claim_index{0}; claim_index < fabric.claims.size() ; ++ claim_index)
    {
        bool is_single = true;
        Rectangle claim = fabric.claims[claim_index];

        for (int y = claim.coordinates.second; y < claim.coordinates.second + claim.size.second; y++)
        {
            for (int x = claim.coordinates.first; x < claim.coordinates.first + claim.size.first; x++)
            {
                if (fabric.fabric[y][x] != 1)
                    is_single = false;
            }
        }
        if (is_single)
        {
            return claim_index + 1;
        }
    }
}

int get_overlapping(std::ifstream &ifstream)
{
    Fabric fabric;
    std::string line;

    while( std::getline(ifstream, line))
    {
        parse_line(fabric, line);
    }

    int counter{0};
    for (auto row : fabric.fabric)
    {
        for (auto sq_inch : row)
        {
            if (sq_inch >= 2)
            {
                counter++;
            }
        }
    }

    // I'm fucking lazy:
    std::cout << get_single_claim(fabric) <<std::endl;

    return counter;

}

void parse_line(Fabric &fabric, std::string line)
{
    std::string delimiter = "@";  // For the first one
    short idx = line.find(delimiter);

    // -1 and +1 to escape whitespaces
    std::string id = line.substr(0, idx - 1);
    line.erase(0, idx + 1);

    delimiter = ":";
    idx = line.find(delimiter);

    std::string coordinates = line.substr(0, idx);
    line.erase(0, idx + 2);  // To remove : and space
    std::string square_size = line;

    Rectangle new_rectangle(coordinates, square_size);
    fabric.add_rectangle(new_rectangle);
}