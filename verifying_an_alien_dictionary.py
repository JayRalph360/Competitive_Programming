class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a dictionary to store the order of each character in the alien alphabet
        order_dict = {char: index for index, char in enumerate(order)}

        # Iterate through the words and compare adjacent words
        for i in range(1, len(words)):
            prev_word = words[i - 1]
            curr_word = words[i]

            # Compare characters in the current and previous words
            for j in range(min(len(prev_word), len(curr_word))):
                prev_char = prev_word[j]
                curr_char = curr_word[j]

                # If the characters are different, check their order in the alien alphabet
                if prev_char != curr_char:
                    if order_dict[prev_char] > order_dict[curr_char]:
                        return False  # Words are not in sorted order
                    break  # No need to compare further characters

            # Check if the current word is a prefix of the previous word
            if len(prev_word) > len(curr_word) and prev_word.startswith(curr_word):
                return False  # Words are not in sorted order

        return True  # All words are in sorted order
