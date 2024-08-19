while True:
    print("High SCORE TABLE")
    print()
    name = input("Initials > ")
    score = input("Score > ")
    print()

    f = open("high.score","+a")
    f.write(f"{name} {score}")
    f.close()

    print("Added")
    