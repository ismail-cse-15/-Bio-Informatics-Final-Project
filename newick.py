import sys

# Set standard output to file "out.txt"
sys.stdout = open("out.txt", "w")

MODD = 1000000007

def main():
    t = int(input())
    while t:
        nw = input().strip()
        s = []
        n = len(nw)
        print(n)
        c = 1

        i = 0
        while i < n:
            if 'A' <= nw[i] <= 'Z' or '1' <= nw[i] <= '9':
            #if nw[i]!=',' or nw[i]!='(' or nw[i]!=')':
                tem = ''
                m = i
                while m < n:
                    tem += nw[m]
                    m += 1
                    if m >= n or nw[m] == ',' or nw[m] == '(' or nw[m] == ')':
                        m -= 1
                        break
                s.append(tem)
                i = m
            elif nw[i] == ')':
                u = s.pop()
                v = s.pop()
                print(v, "and", u, "are from same hypothetical_ancestor_", c, ".", sep=" ")
                u = "hypothetical_ancestor_" + str(c)
                s.append(u)
                c += 1
            i += 1
        print("\n\n")
        t -= 1


if __name__ == "__main__":
    # Set standard input to file "in.txt"
    sys.stdin = open("in.txt", "r")
    main()
