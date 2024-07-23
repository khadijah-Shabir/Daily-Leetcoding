from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Combine names and heights into tuples
        people = list(zip(names, heights))
        
        # Sort primarily by heights (in descending order), and by names (in ascending order) for tie-breaking
        people.sort(key=lambda x: (-x[1], x[0]))
        
        # Extract sorted names
        sorted_names = [person[0] for person in people]
        
        return sorted_names