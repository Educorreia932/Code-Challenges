#include <bits/stdc++.h>

using namespace std;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  	
  	void preOrder(Node *root) {
		
      	if( root == NULL )
          	return;
      
      	std::cout << root->data << " ";
      	
      	preOrder(root->left);
      	preOrder(root->right);
    }

    Node* insert(Node* root, int data) {
        Node N = *root;
        Node* n = &N;

        while (true) {
            if (data < n->data) {
                if (n->left == NULL) {
                    n->left = &Node(data);
                    break;                    
                }

                n = n->left;
            }
                
            else if (data > n->data) {
                if (n->right == NULL) {
                    n->right = &Node(data);
                    break;
                }

                n = n->right;
            }            

            else 
                break;
        }

        return root;
    }

};


int main() {
  
    Solution myTree;
    Node* root = NULL;
    
    int t;
    int data;

    std::cin >> t;

    while(t-- > 0) {
        std::cin >> data;
        root = myTree.insert(root, data);
    }
  	
    myTree.preOrder(root);
  
    return 0;
}
