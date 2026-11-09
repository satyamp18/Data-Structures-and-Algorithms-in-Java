import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        # Segment Tree
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        # Initially all servers are available
        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # Update server availability
        def update(idx, value):
            idx += size
            tree[idx] = value

            idx //= 2
            while idx:
                tree[idx] = tree[2 * idx] + tree[2 * idx + 1]
                idx //= 2

        # Count available servers in [0, end)
        def prefix_sum(end):
            left = size
            right = size + end
            result = 0

            while left < right:
                if left & 1:
                    result += tree[left]
                    left += 1

                if right & 1:
                    right -= 1
                    result += tree[right]

                left //= 2
                right //= 2

            return result

        # Find the index of the kth available server
        def find_kth(kth):
            node = 1

            while node < size:
                if tree[2 * node] >= kth:
                    node = 2 * node
                else:
                    kth -= tree[2 * node]
                    node = 2 * node + 1

            return node - size

        busy = []
        handled = [0] * k

        for i in range(len(arrival)):
            current_time = arrival[i]

            # Release servers whose tasks are completed
            while busy and busy[0][0] <= current_time:
                finish, server = heapq.heappop(busy)
                update(server, 1)

            # Drop request if all servers are busy
            if tree[1] == 0:
                continue

            start = i % k

            # Find the first available server >= start
            before = prefix_sum(start)
            total = tree[1]

            if before < total:
                server = find_kth(before + 1)
            else:
                # Wrap around to the beginning
                server = find_kth(1)

            # Assign request
            handled[server] += 1
            update(server, 0)

            finish_time = current_time + load[i]
            heapq.heappush(busy, (finish_time, server))

        # Find busiest servers
        maximum = max(handled)

        return [
            i for i in range(k)
            if handled[i] == maximum
        ]