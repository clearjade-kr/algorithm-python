class Solution:
    def isNumber(self, s: str) -> bool:
        list_number = '0123456789'

        def check_int(target):
            # If one more sign char, return False
            if target and target[0] in '-+':
                return False

            for ch in target:
                if ch not in list_number:
                    return False
            return True

        def check_float(target):
            # If one more sign char, return False
            if target and target[0] in '-+':
                return False

            # Check floating point in target
            list_split_point = target.split('.')
            if len(list_split_point) == 1:
                return check_int(target=target)
            if len(list_split_point) > 2:
                return False
            target_front, target_back = list_split_point[0], list_split_point[1]
            if target_front:
                if not check_int(target_front):
                    return False
            elif not target_back:
                return False
            if target_back and not check_int(target_back):
                return False
            return True

        # Split with exponent notation and investigate
        s = s.lower()
        if s[0] in '-+':
            s = s[1:]
        if not s:
            return False
        list_split_exp = s.split('e')
        if len(list_split_exp) == 1:
            # No exponent notation
            target = list_split_exp[0]
            if '.' in target:
                return check_float(target=target)
            else:
                return check_int(target=target)

        elif len(list_split_exp) == 2:
            # Single exponent notation
            target_float, target_int = list_split_exp[0], list_split_exp[1]
            if target_int and target_int[0] in '-+':
                target_int = target_int[1:]
            if not target_float or not target_int:
                return False
            if not check_float(target=target_float):
                return False
            if not check_int(target=target_int):
                return False
            return True
        else:
            # More than one exponent notation, return False
            return False


if __name__ == "__main__":
    sol = Solution()
    s = "e3"
    print(sol.isNumber(s=s))
