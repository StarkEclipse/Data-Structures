# 1. Enqueue 
# Enqueue = Add an element to the queue.

# 2. Dequeue
# Dequeue = Remove the element from the front.
# A B C D Remove the front element so A goes away first

# 3. Front
# Front = The first element in the queue.

# 4. Rear
# Rear = The last element in the queue.

# queue = []
# queue.append("Alice")
# queue.append("Bob")
# queue.append("Charlie")

# front = queue[0]
# print(front)

# rear = queue[-1]
# print(rear)

# queue.pop(0)
# print(queue)

orders = []

# Add three orders
orders.append("Order 1")
orders.append("Order 2")
orders.append("Order 3")
# Print the front order
front = orders[0]
print(f"Current order: {front}")

# Print the rear order
rear = orders[-1]
print(f"Last order: {rear}")

# Remove the first order
orders.pop(0)

# Print the remaining orders
print(orders)