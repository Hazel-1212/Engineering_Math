import figure01, figure02, figure03 
import matplotlib.pyplot as plt

print("*"*20)
print("This is the main file for the NYCU-113511170 project.")
print("This project is about calculating the probability of throwing a square.")
print("The project is divided into three figures: figure01, figure02, and figure03.")
print("*"*20)

while True:
    print()
    print("Please enter the command:")
    print("1. Watch Figure 01")
    print("2. Watch Figure 02")
    print("3. Watch Figure 03")
    print("4. Run and save all figures.")
    print("5. Exit")    
    print()
    option = input("Enter your choice (1-5): ")
    if option == "1":
        figure01.main()
    elif option == "2":
        figure02.main()
    elif option == "3":
        print("Wait for a while ...")
        figure03.main()
    elif option == "4":
        figure01.main()
        plt.savefig("113511170_figure01.png")
        figure02.main()
        plt.savefig("113511170_figure02.png")
        print("Wait for a while ...")
        figure03.main()
        plt.savefig("113511170_figure03.png")
        print("All figures saved as PNG files.")
    elif option == "5":
        print("Exiting the program. Goodbye!")
        break