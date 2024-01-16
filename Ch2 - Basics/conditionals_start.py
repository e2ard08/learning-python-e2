#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else

    # if x < y:
    #     result = "X is less than y"
    # elif x == y:
    #     result = "X is the same as Y"    
    # else: 
    #     result = "X is greater than Y"
    # print (result)

    # conditional statements let you use "a if C else b"
    
    # result = "X is less than y" if x < y else "X is greater or equal to y"
    # print (result)


    # match-case makes it easy to compare multiple values
    value = "42"
    match value:
        case "one":
          result = 1
        case "two":
          result = 2
        case "three" | "four":
          result =(3,4)
        case _:
          result = -1
    print (result)


if __name__ == "__main__":
    main()
