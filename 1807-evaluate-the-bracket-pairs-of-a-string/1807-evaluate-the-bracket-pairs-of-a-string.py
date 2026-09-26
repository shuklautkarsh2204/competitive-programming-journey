class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        kd = dict(knowledge)
        res = ""
        i = 0
        while i < len(s):
            if s[i] == '(':
               j = s.find(')',i)
               key = s[i+1 : j]
               res += kd.get(key , "?")
               i = j+1
            else:
                res += s[i]
                i+=1
        return res        

            

        