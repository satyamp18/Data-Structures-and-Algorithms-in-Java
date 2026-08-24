class Solution:

  def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
    index_map = {restaurant: i for i, restaurant in enumerate(list1)}
    min_sum = float("inf")
    result = []

    for j, restaurant in enumerate(list2):
      if restaurant in index_map:
        current_sum = j + index_map[restaurant]
        if current_sum < min_sum:
          min_sum = current_sum
          result = [restaurant]
        elif current_sum == min_sum:
          result.append(restaurant)

    return result