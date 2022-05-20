#include <iostream>
#include <vector>

void lucky_nums(std::vector<unsigned>& odds, unsigned index = 1) {
    if (odds[index] > odds.size())
        return;
    unsigned marker = odds[index];
    std::vector<unsigned > nxt_level;
    for(auto i = 0u; i < odds.size(); ++i)
        if ((i + 1) % marker != 0) nxt_level.push_back(odds[i]);
    odds.swap(nxt_level);
    lucky_nums(odds, index + 1);
}

int main() {



    auto n = 10000u;
    std::vector<unsigned> odds;
    for (auto i = 1u; i < n; i += 2)
        odds.push_back(i);

    lucky_nums(odds);

    for (auto& num: odds)
        std::cout << num << " ";

    std::cout << std::endl;

    auto value = std::upper_bound(odds.begin(), odds.end(), 5);
    std::cout << *value << std::endl;



    return 0;
}
