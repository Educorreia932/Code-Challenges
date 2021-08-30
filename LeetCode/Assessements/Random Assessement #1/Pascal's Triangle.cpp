#include <vector>

using namespace std;

class Solution {
    public:
        vector<vector<int>> generate(int numRows) {
            vector<vector<int>> rows = { { 1 } };

            if (numRows >= 2)
                rows.push_back(vector<int> { 1, 1 });

            for (int i = 2; i < numRows; i++) {
                vector<int> row(i + 1);
                
                row[0] = 1;
                row[i] = 1;

                for (int j = 1; j < i; j++) 
                    row[j] = rows[i - 1][j - 1] + rows[i - 1][j];

                rows.push_back(row);
            }

            return rows;
        }
};
