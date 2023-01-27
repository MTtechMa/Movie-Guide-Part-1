# Kristen Anderson
# CIS 261
# Week 4 Lab Movie Guide

def display_menu():
    print("---The Movie Guide Program---")
    print()
    print("-COMMAND MENU-")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()

def list(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie}")
    print()

def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added.\n")
    return movie_list
    print()
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
        return movie_list
        print()
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie} was deleted.\n")
        return movie_list
        print()

def main():
    movie_list = ["The Cat in the Hat",
                  "Full Metal Jacket",
                  "A Scanner Darkly"]
    
    display_menu()

    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)   
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)  
        elif command.lower() == "exit":
            break
        else:
            print("Invalid command. Please try again.\n")

    print("Goodbye!")

if __name__ == "__main__":
    main()
