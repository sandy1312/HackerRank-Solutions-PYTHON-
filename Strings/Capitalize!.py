# Complete the solve function below.
def solve(s):
    # return s.title()
    return ' '.join(map(str.capitalize, s.split(' ')))
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)



