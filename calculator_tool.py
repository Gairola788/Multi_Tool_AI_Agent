
def calculate_Agent(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"

    except:
        return "Invalid mathematical expression."