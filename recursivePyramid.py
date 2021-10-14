
def run():
    def recursivePyramid(lower: int,upper: int,margin: int =0):
        blanks = " "*margin
        print(blanks, lower, upper)
        if lower>upper:
            print(blanks, 0)
            return 0
        else:
            result = lower + recursivePyramid(lower+1,upper,margin+4)
            print(blanks, result)
            return result
    
    recursivePyramid(1,4)

if __name__ == "__main__":
    run()