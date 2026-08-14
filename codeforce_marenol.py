
class solution:
    def marenol(self, a: str ,b: str) -> bool:
        if a.count('1') != b.count('1'):
            return False
        total_a = sum(i for i in range(len(a)) if a[i] == '1')
        total_b = sum(i for i in range(len(b)) if b[i] == '1')
        return total_a%2 == total_b%2
    
