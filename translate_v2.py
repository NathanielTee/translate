from googletrans import Translator, LANGUAGES

def translate_text():
    translator = Translator()
    
    while True:
        print("\nPilih opsi:")
        print("1. Masukkan teks dan terjemahkan ke bahasa pilihan")
        print("2. Keluar")
        
        choice = input("Masukkan pilihan (1/2): ")

        if choice == "1":
            text = input("Masukkan teks yang ingin diterjemahkan: ")
            print("\nBahasa yang tersedia: ")
            
            # Menampilkan daftar bahasa yang tersedia
            for code, language in LANGUAGES.items():
                print(f"{language.capitalize()} ({code})")
            
            # Meminta input bahasa tujuan dari user
            language_input = input("\nMasukkan nama bahasa tujuan (misal: English, French, Japanese): ").lower()

            # Mencari kode bahasa berdasarkan nama bahasa yang diinput
            dest_language = None
            for code, language in LANGUAGES.items():
                if language_input == language.lower():
                    dest_language = code
                    break

            if dest_language:
                # Menerjemahkan teks ke bahasa yang dipilih
                translation = translator.translate(text, dest=dest_language)
                print(f"\nTerjemahan ke {language_input.capitalize()}: {translation.text}")
            else:
                print("Bahasa tidak ditemukan, coba lagi.")
        
        elif choice == "2":
            print("Program keluar. Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

if __name__ == "__main__":
    translate_text()
