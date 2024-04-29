def removeBrackets(Exp):
    # Code here
    s = list(Exp)
    n = len(Exp)

    ans = [1] * (n + 1)
    lasta = [0] * (n + 1)
    nxta = [0] * (n + 1)

    l = -1

    # Start Iterating from
    # starting index
    for i in range(n):
        lasta[i] = l
        if s[i] == "*" or s[i] == "+" or s[i] == "-" or s[i] == "/":
            l = s[i]

    # Start Iterating from
    # last index
    l = -1

    for i in range(n - 1, -1, -1):
        nxta[i] = l
        if s[i] == "*" or s[i] == "+" or s[i] == "-" or s[i] == "/":
            l = s[i]

    stack = []
    sign = [-1] * 256
    mp = [0] * 256
    operand = ["*", "+", "-", "/"]

    for p in range(n):
        for x in operand:
            mp[ord(x)] = 0
            if x == s[p]:
                sign[ord(x)] = p
        if s[p] == "(":
            stack.append(p)

        elif s[p] == ")":
            i = stack.pop()
            j = p

            nxt = nxta[j]
            last = lasta[i]

            # Iterate in operator
            # array
            for x in operand:
                if sign[ord(x)] >= i:
                    mp[ord(x)] = 1
            ok = 0

            if i > 0 and j + 1 < n and s[i - 1] == "(" and s[j + 1] == ")":
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
            elif mp[ord("-")] == 0 and mp[ord("+")] == 0:
                ok = 1
            else:
                if (last == -1 or last == "+" or last == "-") and (
                    nxt == -1 or nxt == "+" or nxt == "-"
                ):
                    ok = 1
            # If the pair is reduntant
            if ok == 1:
                ans[i] = 0
                ans[j] = 0

    # Final string
    res = ""
    for i in range(n):
        if ans[i] > 0:
            res += s[i]
    return res


expr1 = "1*(2+(3*(4+5)))"
expr2 = "2 + (3 / -5)"
expr3 = "x+(y+z)+(t+(v+w))"

# Function call
result = removeBrackets(expr3)
print(result)
