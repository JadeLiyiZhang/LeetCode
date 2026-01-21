/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int goodNodes(TreeNode* root) {
        return nodeCount(root, INT_MIN);
    }

    int nodeCount(TreeNode* node, int highest) {
        if (node == NULL) return 0;
        if (node->val >= highest) {
            return 1 + nodeCount(node->left, node->val) + nodeCount(node->right, node->val);
        }
        return nodeCount(node->left, highest) + nodeCount(node->right, highest);
    }
};