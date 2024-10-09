def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0 or carry:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            
            value = x1 + x2 + carry
            carry = value // 10
            result.append(value % 10)
            
            p1 -= 1
            p2 -= 1
        
        return ''.join(str(x) for x in result[::-1])
