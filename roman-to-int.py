def romanToInt(self, s: str) -> int:
        roman_values = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000  
        }
        t_value = 0
        len_numeral_str = len(s)

        for i in range(len_numeral_str):
        # substracting it if the current value is smaller than the next value
            if i < len_numeral_str - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                t_value -= roman_values[s[i]]
            else:
                # or adding it to the result
                t_value += roman_values[s[i]]
        return t_value
