"""There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required for all the customers to check out!
input
customers: an array of positive integers representing the queue.
Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required."""
# def queue_time(customers, n):
#     if not customers:
#         return 0
#     if len(customers) <= n:
#         return max(customers)
#     else:
#         return sum(customers) / n

def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)


# print(queue_time([], 1))
# print(queue_time([5], 1))
# print(queue_time([2], 5))
# print(queue_time([1, 2, 3, 4, 5], 1))
# print(queue_time([1, 2, 3, 4, 5], 100))
# print(queue_time([2, 2, 3, 3, 4, 4], 2))
print(queue_time([46, 4, 33, 35, 44, 39, 46, 12, 18, 50, 12], 3))