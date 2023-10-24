def magic_calculation(a, b):
    result = 0
    for i in range(1, 4):
        try:
            if a > i:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
        else:
            result += b
        finally:
            result += 1
    return result
