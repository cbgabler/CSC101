

def float_default(string, float_number):
    try:
        result = float(string)
        return result
    except ValueError:
        return float_number

