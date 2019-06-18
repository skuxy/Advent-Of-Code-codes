//
// Created by skux on 05.12.18..
//

#include "main.h"

class Guard
{
public:
    Guard()
    {

    }

public:
    int id;
    int minutes_slept{0};
    int *minutes_spent_sleeping;

public:
    Guard(int id)
    {
        this->id = id;

        int minutes_slept[60] = {};
        this-> minutes_spent_sleeping =  minutes_slept;
    }

    void new_sleep(int minute_sleeps, int minute_wakes)
    {

        for (int minute_sleeping = minute_sleeps ; minute_sleeping < minute_wakes ; minute_sleeping ++)
        {
            this->minutes_spent_sleeping[minute_sleeping] ++ ;
            this->minutes_slept ++ ;
        }
    }
};

std::vector<std::string> get_sorted_lines(std::ifstream &ifstream);

int get_id_x_minute(std::ifstream &ifstream)
{
    auto lines = get_sorted_lines(ifstream);

    Guard current_guard;
    int sleep_start{0};
    int sleep_stop{0};
    std::map<int, Guard> guards;

    for (std::string line : lines)
    {
        auto action = line.substr(19, 5);

        if (action == "Guard")
        {
            // this shouldn't pass for single or double digits, but it does. Why? Dunno
            int id = std::stoi(line.substr(26, 4));

            if (guards.count(id) == 0)
            {
                guards.insert(std::make_pair(id, Guard(id)));
            }
            current_guard = guards[id];
        }
        else if (action == "falls")
        {
            sleep_start = stoi(line.substr(15,2));
        }
        else if (action == "wakes")
        {
            sleep_stop = stoi(line.substr(15,2));
            current_guard.new_sleep(sleep_start, sleep_stop);
        }
    }

    Guard max_sleeper;
    for(auto it = guards.begin() ; it != guards.end() ; it ++)
    {
        Guard guard = it->second;
        if (guard.minutes_slept > max_sleeper.minutes_slept)
        {
            max_sleeper = guard;
        }
    }

    int most_slept_minute = 0;
    for (int curr_min = 0 ; curr_min < 60 ; curr_min++)
    {
        if (curr_min > most_slept_minute)
        {
            most_slept_minute = curr_min;
        }
    }

    return max_sleeper.id * most_slept_minute;
}

std::vector<std::string> get_sorted_lines(std::ifstream &ifstream)
{
    std::vector<std::string> lines;
    std::string line;

    while (getline(ifstream, line))
    {
        lines.push_back(line);
    }

    sort(lines.begin(), lines.end());

    return lines;
}


