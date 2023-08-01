from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    queue = deque([0])  # Start with the first box (boxes[0])

    while queue:
        current_box = queue.popleft()
        visited[current_box] = True

        for key in boxes[current_box]:
            if not visited[key]:
                queue.append(key)

    return all(visited)

