import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return

        n, k, l, c, d, p, nl, np = map(int, line.strip().split())

        total_drink_ml = k * l
        total_lime_slices = c * d
        
        toasts_from_drink = total_drink_ml // nl
        toasts_from_limes = total_lime_slices // 1
        toasts_from_salt = p // np
        
        total_toasts_possible = min(toasts_from_drink, toasts_from_limes, toasts_from_salt)
        
        toasts_per_friend = total_toasts_possible // n
        
        print(toasts_per_friend)

    except EOFError:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    solve()
