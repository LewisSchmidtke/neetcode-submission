class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        neg_heap = []

        current_balance = 0
        transaction_count = 0

        for transaction in transactions:
            current_balance += transaction
            transaction_count += 1

            if transaction < 0:
                heapq.heappush(neg_heap, transaction)

            if current_balance < 0:
                current_balance -= heapq.heappop(neg_heap)
                transaction_count -= 1

        return transaction_count

