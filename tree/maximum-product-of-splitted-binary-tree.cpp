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
    int maxProduct(TreeNode* root) {
        const int kMod = 1e9 + 7;
        function<int(TreeNode*)> sum = [&sum](TreeNode* r) {
            if (!r) return 0;
            return r->val + sum(r->left) + sum(r->right);
        };
        long s = sum(root);
        long ans = 0;
        function<int(TreeNode*)> solve = [&](TreeNode* r) {
            if (!r) return 0;
            int sl = solve(r->left);
            int sr = solve(r->right);
            ans = max({ans, (s - sl) * sl, (s - sr) * sr});
            return r->val + sl + sr;
        };
        solve(root);
        return ans % kMod;
    }
};