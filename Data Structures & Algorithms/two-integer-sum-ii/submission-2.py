class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        half = target / 2
        expect = []
        for i in numbers:
            compilentary = target - i
            if i == half:
                continue
            if i in expect:
                i_index = numbers.index(i)
                expect_index = numbers.index(compilentary)
                i_index += 1
                expect_index += 1

                soloution = [expect_index,i_index]
                return soloution
            expect.append(compilentary)