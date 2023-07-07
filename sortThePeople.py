class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Create a list of tuples (name, height)
        people = list(zip(names, heights))

        # Sort the list of tuples in descending order by height
        people.sort(key=lambda x: x[1], reverse=True)

        # Extract only the names from the sorted list
        sorted_names = [name for name, _ in people]

        return sorted_names
