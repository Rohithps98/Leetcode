class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        bob_time = [float('inf')] * n
        def calc_bob_path(node, parent, time):
            if node == 0:
                bob_time[node] = time
                return True   
            for neighbor in graph[node]:
                if neighbor != parent:
                    if calc_bob_path(neighbor, node, time + 1):
                        bob_time[node] = time
                        return True
            return False
        calc_bob_path(bob, -1, 0)
        def dfs(node, parent, time, income):
            current_income = 0
            if time < bob_time[node]:
                current_income = amount[node]
            elif time == bob_time[node]:
                current_income = amount[node] / 2
            total_income = income + current_income
            is_leaf = True
            child_max = float('-inf')
            for neighbor in graph[node]:
                if neighbor != parent:
                    is_leaf = False
                    child_result = dfs(neighbor, node, time + 1, total_income)
                    child_max = max(child_max, child_result)
            if is_leaf:
                return total_income
            else:
                return child_max
        result = dfs(0, -1, 0, 0)
        return int(result)