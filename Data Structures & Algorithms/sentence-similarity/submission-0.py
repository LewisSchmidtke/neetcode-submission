class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        pointer = 0

        while pointer < len(sentence1):
            if sentence1[pointer] != sentence2[pointer]:
                if pointer >= len(similarPairs):
                    return False

                mapping = set(similarPairs[pointer])
                if sentence1[pointer] not in mapping or sentence2[pointer] not in mapping:
                    return False

            pointer += 1

        return True
