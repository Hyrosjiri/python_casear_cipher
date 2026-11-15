# Importy knihoven
import os
import string


# Znaková sada pro šifrování
CHARACTERS = (
    string.ascii_letters +
    string.digits +
    string.punctuation +
    "áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ"
)

# Vyčištění terminálu
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Výběr režimu
def get_mode():
    while True:
        mode = input("Zadej 'Encrypt' nebo 'Decrypt': ").strip().lower()
        
        if mode in ('encrypt', 'decrypt'):
            return mode
        
        print("[CHYBA] Neplatný vstup")

# Zadání posunu
def get_shift():
    while True:
        try:
            return int(input("Zadej číselný posun: "))
        except ValueError:
            print("[CHYBA] Neplatný vstup")

# Zadání zprávy
def get_message():
    return input("Zadej zprávu: ")

# Šifrování a dešifrování zprávy
def caesar_cipher(mode, shift, message):
    if mode == 'decrypt':
        shift *= -1
        
    shifted_text = ""

    for char in message:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            new_index = (index + shift) % len(CHARACTERS)
            shifted_text += CHARACTERS[new_index]

        else:
            shifted_text += char
    return shifted_text

# Hlavní program
def main():
    clear_screen()
    mode = get_mode()
    shift = get_shift()
    message = get_message()
    
    result = caesar_cipher(mode, shift, message)

    clear_screen()
    print(f"Výsledná zpráva: {result}")
    
    input("[\nENTER] - Ukončit")

# Spuštění programu
if __name__ == "__main__":
    main()