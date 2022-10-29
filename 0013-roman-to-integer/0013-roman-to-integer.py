class Solution:
    def romanToInt(self, s: str) -> int:
        #Game plan for O(N) Solution.
        
        #Create a Hashmap and map the values.
        roman_integers = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        } #This is O(1) because we have only 7 values.
        
        total = 0 #Total of the strings.
        
        #A loop to loop over the values linearly to check in the hashmap.
        for i in range(len(s)):
            
            #if the i + 1 is in the bound and the roman integer's value of left,
            #is lesser than the value of integer on right.
            #Then subtract it from the result.
            if i + 1 < len(s) and roman_integers[s[i]] < roman_integers[s[i + 1]]:
                total -= roman_integers[s[i]]
            
            #Else add it to the result.
            else:
                total += roman_integers[s[i]]
        
        #return the total in the end.        
        return total