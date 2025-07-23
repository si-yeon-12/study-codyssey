def main():
    num_str = input("Input:")
    num = []
    try:
        num_str = num_str.split()
        for i in num_str:
            num.append(float(i))
    except:
        print("Invalid input.")
        return 0
    
    max = num[0] 
    min = num[0]

    for i in range(len(num)):
        if num[i] > max:
            max = num[i]
        if num[i] < min:
            min = num[i]

    print("Min:", min, ",Max:", max)

if __name__ == "__main__":
    main()
