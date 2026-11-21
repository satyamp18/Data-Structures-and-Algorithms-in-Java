from typing import List


class Solution:

  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    n = len(parent)

    # 1. Build the initial tree
    adj = [[] for _ in range(n)]
    for i in range(1, n):
      adj[parent[i]].append(i)

    # 2. Find the new parent for each node via DFS while tracking
    #    the most recent ancestor for each character 'a'-'z'.
    new_parent = parent[:]
    last_seen = [-1] * 26

    def dfs_find_parents(u: int) -> None:
      c = ord(s[u]) - ord("a")
      prev = last_seen[c]

      if prev != -1:
        new_parent[u] = prev

      last_seen[c] = u
      for v in adj[u]:
        dfs_find_parents(v)
      last_seen[c] = prev  # Backtrack

    dfs_find_parents(0)

    # 3. Build the final tree using the updated parents
    final_adj = [[] for _ in range(n)]
    for i in range(1, n):
      final_adj[new_parent[i]].append(i)

    # 4. Compute subtree sizes in the final tree
    ans = [1] * n

    def dfs_sizes(u: int) -> int:
      size = 1
      for v in final_adj[u]:
        size += dfs_sizes(v)
      ans[u] = size
      return size

    dfs_sizes(0)
    return ans