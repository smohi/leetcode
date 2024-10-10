def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            columnNumber = columnNumber * 26 + value
        
        return columnNumber
