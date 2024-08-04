import os
import subprocess
import json
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def encrypt_file(input_file, output_file, public_key):
    subprocess.run(['openssl', 'pkeyutl', '-encrypt', '-inkey', public_key, '-pubin', 
                    '-in', input_file, '-out', output_file])

def decrypt_file(input_file, output_file, private_key):
    subprocess.run(['openssl', 'pkeyutl', '-decrypt', '-inkey', private_key, 
                    '-in', input_file, '-out', output_file])

def load_passwords():
    if not os.path.exists("pass_management.bin"):
        return []
    try:
        decrypt_file("pass_management.bin", "temp.json", "private_key_pass_management.pem")
        with open("temp.json", "r") as f:
            content = f.read()
            if not content:
                return []
            passwords = json.loads(content)
        os.remove("temp.json")
        return passwords
    except json.JSONDecodeError:
        print("Erreur lors du chargement des mots de passe. Fichier corrompu ou vide.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []

def save_passwords(passwords):
    with open("temp.json", "w") as f:
        json.dump(passwords, f)
    encrypt_file("temp.json", "pass_management.bin", "public_key_pass_management.pem")
    os.remove("temp.json")

def add_password(passwords):
    while True:
        clear_screen()
        print("--- Ajout d'un nouveau mot de passe ---")
        password = input("Entrez le mot de passe à ajouter: ")
        passwords.append(password)
        save_passwords(passwords)
        print("Mot de passe ajouté et chiffré.")
        choice = input("Appuyez sur 'C' pour continuer l'ajout ou 'Q' pour quitter: ").lower()
        if choice != 'c':
            break

def display_passwords(passwords):
    clear_screen()
    if not passwords:
        print("\n" + "_" * 30)
        print("Aucun mot de passe enregistré.")
        print("_" * 30)
    else:
        print("\n" + "_" * 30)
        print("Mots de passe:")
        print("_" * 30)
        for i, password in enumerate(passwords, 1):
            print(f"  {i}. {password}")
        print("_" * 30)
    input("Appuyez sur Entrée pour continuer...")

def delete_password(passwords):
    while True:
        clear_screen()
        print("--- Suppression d'un mot de passe ---")
        display_passwords(passwords)
        if not passwords:
            input("Appuyez sur Entrée pour revenir au menu principal...")
            return
        try:
            index = int(input("Entrez le numéro du mot de passe à supprimer (0 pour quitter): ")) - 1
            if index == -1:
                break
            if 0 <= index < len(passwords):
                deleted = passwords.pop(index)
                save_passwords(passwords)
                print(f"Mot de passe '{deleted}' supprimé.")
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        choice = input("Appuyez sur 'C' pour continuer la suppression ou 'Q' pour quitter: ").lower()
        if choice != 'c':
            break

def print_header():
    print("\n" + "=" * 50)
    print("     GESTIONNAIRE DE MOTS DE PASSE SÉCURISÉ")
    print("=" * 50)

def print_menu():
    print("\n" + "-" * 40)
    print("Menu Principal:")
    print("-" * 40)
    print("1. Ajouter un mot de passe")
    print("2. Afficher les mots de passe")
    print("3. Supprimer un mot de passe")
    print("4. Quitter")
    print("-" * 40)

def main():
    passwords = load_passwords()
    while True:
        clear_screen()
        print_header()
        print_menu()
        choice = input("Choisissez une option: ")

        if choice == "1":
            add_password(passwords)
        elif choice == "2":
            display_passwords(passwords)
        elif choice == "3":
            delete_password(passwords)
        elif choice == "4":
            clear_screen()
            print("\nMerci d'avoir utilisé le gestionnaire de mots de passe!")
            print("Au revoir!")
            break
        else:
            print("\n/!\\ Option invalide. Veuillez réessayer.")
            input("Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
