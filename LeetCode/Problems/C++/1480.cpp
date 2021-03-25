#include <vector>

using namespace std;

class Solution {
    public:
        vector<int> runningSum(vector<int>& nums) {
            vector<int> result;
            int partial_sum = 0;
            
            for (int num : nums) {
                partial_sum += num;

                result.push_back(partial_sum);
            }

            return result;
        }
};