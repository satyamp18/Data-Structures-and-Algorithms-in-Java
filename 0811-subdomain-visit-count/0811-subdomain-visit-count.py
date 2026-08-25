from collections import defaultdict


class Solution:

  def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
    counts = defaultdict(int)

    for entry in cpdomains:
      count_str, domain = entry.split(" ")
      count = int(count_str)

      fragments = domain.split(".")
      for i in range(len(fragments)):
        subdomain = ".".join(fragments[i:])
        counts[subdomain] += count

    return [f"{count} {subdomain}" for subdomain, count in counts.items()]