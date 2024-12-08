
running = True

def search(term, file_name):
    flag = False # to mark if found
    result = [] # to store search result

    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.lower().find(term.strip().lower()) != -1:
                flag = True
                result.append(line)

    if flag == False:
        print(f"""
Your search term {term} doesn't exist in file {file_name}.
    """)
    else:
        invalid = True
        while invalid:
            show = input(f"""
Your search term {term} exists in file {file_name}!
Would you like to see the entries? ( y / n )
        """)
            if show == "y":
                for line in result:
                    print(line)
                return
            elif show == "n":
                return
            else:
                print("Invalid input.")
        

while running:
    source = input(f"""
What file are you looking for?
    a) 60s-music file
    b) athelets file
    x) exit
""")

    if source == "a":
        term = input("Enter the search term for 60s-music file:")
        search(term, "60s_music.csv")
    elif source == "b":
        term = input("Enter the search term for athelets file:")
        search(term, "athelets.csv")        
    elif source == "x":
        running = False
    else:
        print("Invalid input.")

