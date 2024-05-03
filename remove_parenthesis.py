import unittest


def removeBrackets(Exp):
    # Code here
    exp_list = list(Exp)
    n = len(Exp)

    answer = [1] * (n + 1)
    lasta = [0] * (n + 1)
    nxta = [0] * (n + 1)
    operator = ["*", "+", "-", "/"]

    l = -1  # initial value

    # Start Iterating from
    # starting index
    for i in range(n):
        lasta[i] = l
        if exp_list[i] in operator:
            l = exp_list[i]

    # Start Iterating from
    # last index
    l = -1

    for i in range(n - 1, -1, -1):
        nxta[i] = l
        if exp_list[i] in operator:
            l = exp_list[i]
    stack = []
    sign = [-1] * 256  # track operator positions
    mp = [0] * 256

    for p in range(n):
        for x in operator:
            mp[ord(x)] = 0
            if x == exp_list[p]:
                sign[ord(x)] = p

        if exp_list[p] == "(":
            stack.append(p)

        elif exp_list[p] == ")":
            i = stack.pop()
            j = p

            nxt = nxta[j]  # next index
            last = lasta[i]

            # Iterate in operator
            # array
            for x in operator:
                if sign[ord(x)] >= i:
                    mp[ord(x)] = 1
            ok = 0

            if (
                i > 0
                and j + 1 < n
                and exp_list[i - 1] == "("
                and exp_list[j + 1] == ")"
            ):
                ok = 1

            if (
                mp[ord("+")] == 0
                and mp[ord("*")] == 0
                and mp[ord("-")] == 0
                and mp[ord("/")] == 0
            ):
                ok = 1

            if last == -1 and nxt == -1:
                ok = 1

            if last == "/":
                pass
            elif last == "-" and (mp[ord("+")] == 1 or mp[ord("-")] == 1):
                pass
            elif mp[ord("+")] == 0:
                ok = 1

            else:
                if (last == -1 or last == "+" or last == "-") and (
                    nxt == -1 or nxt == "+" or nxt == "-"
                ):

                    ok = 1

            # If the pair is reduntant
            if ok == 1:
                answer[i] = 0
                answer[j] = 0

    # Final string
    result = ""
    for i in range(n):
        if answer[i] > 0:
            result += exp_list[i]
    return result


class TestRemoveBrackets(unittest.TestCase):

    def test_remove_brackets(self):
        # Test cases
        test_cases = [
            ("1*(2+(3*(4+5)))", "1*(2+3*(4+5))"),
            ("2 + (3 / -5)", "2 + 3 / -5"),
            ("x+(y+z)+(t+(v+w))", "x+y+z+t+v+w"),
            ("(2*(3+4)*5)/6", "2*(3+4)*5/6"),
            ("(-5)/7", "-5/7"),
            ("(-5)*7", "-5*7"),
            ("1+(-1)", "1+(-1)"),
            ("5*(-3)", "5*-3"),
            ("((2*((2+3)-(4*6))+(8+(7*4))))", "2*(2+3-4*6)+8+7*4"),
        ]
        # Iterate through test cases and check the result
        for input_expr, expected_output in test_cases:
            with self.subTest(input_expr=input_expr, expected_output=expected_output):
                result = removeBrackets(input_expr)
                self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
