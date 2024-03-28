import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Please enter the desired password length: "))
        if length <= 0:
            print("Please enter a valid positive number.")
            return
        password = generate_password(length)
        print("Generiertes Passwort:", password)
    except ValueError:
        print("Please enter a valid positive number.")

if __name__ == "__main__":
    main()
##########################################################################################################################
#           __               _______      __________         _____________   ____            ___   ___    ___________    #
#          /  \             /  ____  \   /  ______  \       /  _______   /  /    \          /  /  /__/   /  ________/    #
#         /    \           /  /   /  /  /  /      \  \     /  /      /  /  /  /\  \        /  /  ___    /  /             #  
#        /  /\  \         /  /___/  /  /  /        \  \   /  /      /  /  /  /  \  \      /  /  /  /    \  \________     #
#       /  /__\  \       /     ____/  /  /         /  /  /  /      /  /  /  /    \  \    /  /  /  /      \________  \    #
#      /  ______  \     /  /\  \     /  /         /  /  /  /      /  /  /  /      \  \  /  /  /  /               /  /    # 
#     /  /      \  \   /  /  \  \   /  /_________/  /  /  /______/  /  /  /        \  \/  /  /  /        ______ /  /     #
#    /__/        \__\ /__/    \__\ /_______________/  /____________/  /__/          \____/  /__/        /_________/      #
#                                                                                                                        #
##########################################################################################################################