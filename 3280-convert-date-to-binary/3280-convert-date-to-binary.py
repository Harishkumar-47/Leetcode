class Solution:
    def convertDateToBinary(self, date: str) -> str:
        s = ""
        dates = date.split('-')
        length = len(dates)
        for i in range(length):
            ij = bin(int(dates[i]))[2:]
            s += str(ij)
            if i != length-1:
                s += '-'
        return s