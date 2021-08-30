// WIP

#include <queue>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    public:
        int widthOfBinaryTree(TreeNode* root) {
            int max_width = 1;
            queue<TreeNode*> q; 

            q.push(root);

            while (!q.empty()) {
                int width = 1;

                TreeNode* node = q.front();
                q.pop();

                if (node->left) {
                    q.push(node->left);
                }

                if (node->right) {
                    q.push(node->right);
                }

                if (width > max_width)
                    max_width = width;            
            }

            return max_width;
        }
};
