def main():
    print("What do you intend to get today? ")
    print()
    print("Enter each item individually and press 'Enter',")
    print("repeating the process for the number")
    print("of the specific item you wish to obtain.")
    print("When you're done type 'end'")
    print()

    grocery_list = {}
    while True:
        item = input().upper()
        if item == "END":
            break
        elif item not in grocery_list:
            grocery_list[item] = 1
        else:
            grocery_list[item] += 1
        
    sorted_list = sorted(grocery_list)

    print()
    for good in sorted_list:
        print(grocery_list[good], good)

if __name__ == "__main__":
    main()
