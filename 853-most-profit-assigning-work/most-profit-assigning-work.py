from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Step 1: Pair jobs with their profits and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Step 2: Sort workers by their abilities
        worker.sort()
        
        max_profit = 0  # To store the maximum profit we can achieve
        best_profit = 0  # To keep track of the best profit we can assign so far
        i = 0  # To iterate over the jobs
        
        # Step 3: Assign jobs to workers
        for ability in worker:
            # Find the best job that the worker can do
            while i < len(jobs) and jobs[i][0] <= ability:
                best_profit = max(best_profit, jobs[i][1])
                i += 1
            # Add the best possible profit for this worker to the total profit
            max_profit += best_profit
        
        return max_profit
