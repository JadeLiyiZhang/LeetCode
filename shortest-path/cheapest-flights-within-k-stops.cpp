class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // dp[i][j]: cheapest cost to dst j within i+1 flight.
        vector<vector<int>> dp(k+2, vector<int>(n, INT_MAX/2));
        dp[0][src] = 0;
        int res = INT_MAX/2;
        for (int i=1; i<=k+1; i++){
            for (auto flight:flights){
                int a = flight[0], b = flight[1], p = flight[2];
                dp[i][b] = min(dp[i][b], dp[i - 1][a] + p);
                if (b==dst) res = min(res, dp[i][b]);
            }
        }
        return res == INT_MAX/2 ? -1:res;
    }
};