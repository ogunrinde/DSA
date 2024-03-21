from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)



class IsBalance():
    def __init__(self, text):
        self.text = text

    def is_match(self,ch1, ch2):
        match_dict = {
            '}': '{',
            ')': '(',
            ']':'['
        }
        return match_dict[ch1] == ch2

    def check(self):
        s = Stack()
        for char in self.text:
            if char == "{" or char == "(" or char == "[":
                s.push(char)
            if char == "}" or char == ")" or char == "]":
                if s.size() == 0:
                    return False
                elif self.is_match(char,s.pop()):
                    return True
                else:
                    return False
        return False
                
if __name__ == "__main__":
    is_balanced = IsBalance("({a+b})")
    is_balanced2 = IsBalance("))((a+b}{")
    is_balanced3 = IsBalance("((a+b))")
    is_balanced4 = IsBalance("))")
    is_balanced5 = IsBalance("[a+b]*(x+2y)*{gg+kk}")
    print(is_balanced.check())
    print(is_balanced2.check())
    print(is_balanced3.check())
    print(is_balanced4.check())
    print(is_balanced5.check())