def mysort(lst):
    for j in range(len(lst)-1):
        swqpped = False
        for idx in range(len(lst)-1-j):
            if lst[idx] > lst[idx+1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                swapped = True
        if not swapped:
            break
    return lst

def main():
    num_input = input("Enter numbers :")
    num_fl = []

    try:
        if not num_input.strip():
            print("Invalid input.")
            return 0        
        num_str_list = num_input.split()
        for s in num_str_list:
            num_fl.append(float(s))
    except:
        print("Invalid input.")
        return 0
    
    result = mysort(num_fl)

    print("Sorted:", " ".join(f"<{k}>" for k in result))

if __name__ == "__main__":
    main()
