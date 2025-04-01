from bisect import bisect_left, bisect_right

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & -index
        return sum_val
    
    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)
    
def process_maintenance_logs(maintenance_logs, queries):
    unique_dates = sorted(set(date for _, date, _ in maintenance_logs))
    date_to_index = {date: i + 1 for i, date in enumerate(unique_dates)}

    fenwick_tree = FenwickTree(len(unique_dates))

    for _, date, cost in maintenance_logs:
        fenwick_tree.update(date_to_index[date], cost)

    results = []
    for start_date, end_date in  queries:
        left_idx = bisect_left(unique_dates, start_date) + 1
        right_idx = bisect_right(unique_dates, end_date)
        if left_idx <= right_idx and right_idx > 0:
            results.append(fenwick_tree.range_query(left_idx, right_idx))
        else:
            results.append(0)

    return results

maintenance_logs = [(101, "2024-01-01", 500), (102, "2024-01-10", 300), (101, "2024-01-15", 700)]
queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]

print(process_maintenance_logs(maintenance_logs, queries))
