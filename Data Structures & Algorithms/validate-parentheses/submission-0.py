class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        bracket_pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        expected = []

        for bracket in s:
            if bracket in bracket_pairs.keys():
                closing_bracket = bracket_pairs[bracket]
                expected.insert(0, closing_bracket)
            else:
                try:
                    if expected[0] != bracket:
                        return False
                    else:
                        expected.pop(0)
                except IndexError:
                    return False

        return len(expected) == 0


