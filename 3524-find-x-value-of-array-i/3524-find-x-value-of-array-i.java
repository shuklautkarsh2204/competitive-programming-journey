class Solution {
    public long[] resultArray(int[] nums, int k) {
        long[] result = new long[k];
        // dp[v] stores the number of subarrays ending at the current index with product % k == v
        long[] dp = new long[k];

        for (int num : nums) {
            long[] nextDp = new long[k];
            int curMod = (int) ((long) num % k);

            // Extend existing subarrays
            for (int v = 0; v < k; v++) {
                if (dp[v] > 0) {
                    int nextRem = (int) (((long) v * curMod) % k);
                    nextDp[nextRem] += dp[v];
                }
            }

            // Single element subarray [num]
            nextDp[curMod]++;

            // Accumulate to total result
            for (int v = 0; v < k; v++) {
                result[v] += nextDp[v];
            }

            dp = nextDp;
        }

        return result;
    }
}