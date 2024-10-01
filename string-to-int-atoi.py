def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        s = s.lstrip()  
        
        if not s:
            return 0
        
        sign = 1  
        start = 0  
        
        if s[0] == '-':
            sign = -1  
            start = 1  
        elif s[0] == '+':
            start = 1  
        
        result = 0  
        
        for i in range(start, len(s)):
            if s[i].isdigit():
                result = result * 10 + int(s[i])
                
                if sign == 1 and result > INT_MAX:
                        return INT_MAX  
                if sign == -1 and result > -INT_MIN:
                    return INT_MIN  
            else:
                break
        
        return sign * result
