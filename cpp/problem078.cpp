#include <cmath>
#include <iostream>
#include <list>
#include <vector>


const double ANSWER = 55374;
const int DIVISOR = pow(10, 6);
const bool SLOW = true;


int main() {
    std::vector<std::list<int>> lst = {{1}};
    int i = 0;
    int i_j_1 = 0;
    int sum = 0;
    int lst_i_j_1_0 = 0;
    int lst_i_j_1_1 = 0;
    while(true)
    {
        i += 1;
        std::list<int> new_row = {};
        i_j_1 = i;
        sum = 0;
        for (int j = 0; j < i; ++j)
        {
            i_j_1 -= 1;
            lst_i_j_1_0 = lst[i_j_1].front();
            sum = (sum + lst_i_j_1_0) % DIVISOR;
            new_row.push_back(lst_i_j_1_0);
            if (lst[i_j_1].size() > 1)
            {
                lst[i_j_1].pop_front();
                lst_i_j_1_1 = lst[i_j_1].front();
                lst[i_j_1].pop_front();
                lst[i_j_1].push_front((lst_i_j_1_0 + lst_i_j_1_1) % DIVISOR);
            }
        }
        if (i % 100 == 0)
        {
            std::cout << i << " " << sum << std::endl;
        }
        if (sum == 0)
        {
            std::cout << i << std::endl;
            return i;
        }
        lst.push_back(new_row);
    }
    return 0;
}
