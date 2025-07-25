def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b

def mul_div(lst):
    temp_list = []
    i = 0

    while i < len(lst):
        if lst[i] == '*':
            num_a = temp_list.pop()
            num_b = lst[i+1]
            result = multiply(num_a, num_b)
            temp_list.append(result)
            i += 2
        elif lst[i] == '/':
            num_a = temp_list.pop()
            num_b = lst[i+1]
            result = divide(num_a, num_b)
            temp_list.append(result)
            i += 2
        else:
            temp_list.append(lst[i])
            i += 1

    return temp_list

def add_sub(lst):
    final_result = lst[0]
    j = 1
    while j < len(lst):
        operator = lst[j]
        next_num = lst[j+1]

        if operator == '+':
            final_result = add(final_result, next_num)
        elif operator == '-':
            final_result = subtract(final_result, next_num)
        else:
            raise
        j += 2
    
    return final_result

def main():
    calcul_input = input("Input: ")

    try:
        calcul = calcul_input.split()
        if not calcul:
            raise
        
        calcul_list = []
        for i in calcul:
            try:
                calcul_list.append(float(i))
            except:
                calcul_list.append(i)

        temp_list = mul_div(calcul_list)
        final_result = add_sub(temp_list)

        print("Result: ", final_result)

    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None
    except:
        print("Invalid input.")
        return None

if __name__ == "__main__":
    main()

# priority_calculator 파일 보완
