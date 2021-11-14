from a3 import *

MENU="""
1.Load file
2.Display database
3.Display dictionary
4.Show total cases by dates (0), age groups (1), genders (2)
5.Display data for a PHU
6.Show total cases in PHUs by age groups
7.Show total cases for top-x hotspots
8.Quit the program

Please select a number between 1 - 8. >>
"""

def menu():
    return input(MENU)

def main():
    filename=None
    database=None
    dictionary = None

    while True:
        choice=eval(menu())

        if choice==1:
            filename=input('Enter a file name: ')
            try:
                print("Data loaded successfully.")
                database=return_list(filename)
                dictionary=return_dict(filename)
            except:
                print('Data load failed!! \nTry giving absolute path to file.')
            
        elif choice==2:
            print(display_2Dlist(return_list(filename)))
        elif choice==3:
            print(display_dict(return_dict(filename)))
        elif choice==4:
            index=eval(input("Enter an index: "))
            x,y=get_total_cases(database,index)
            print('Number of cases for each group:')
            print(x)
            print(f'Total cases:{y}')
        elif choice==5:
            PHU_ID=input("Enter a PHU Id: ")
            print(display_PHU_summary(database,dictionary,PHU_ID))
        elif choice==6:
            print(get_cases_by_PHU_and_age(database,dictionary))
        elif choice==7:
            hotspots=eval(input("Enter the number of hotspots:"))
            print(get_topx_hotspots(database,dictionary,hotspots))
        elif choice==8:
            print("Thank you for using this program.")
            exit()


if __name__ == '__main__':
    main()