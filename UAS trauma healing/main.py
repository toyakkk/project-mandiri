from models.users import Pasien
from repositories.pasien_repo import InMemoryPasienRepository
from services.counseling import CounselingService

def main():
    repo = InMemoryPasienRepository()
    service = CounselingService(repo)

    try:
        while True:
            print("\n=== Trauma Healing Counseling CLI ===")
            print("1. Register Pasien")
            print("2. List Pasien")
            print("3. Exit")

            choice = input("Choose Menu: ")

            if choice == "1":
                user_id = int(input("User ID: "))
                name = input("Name: ")
                trauma = input("Trauma Type: ")

                pasien = Pasien(user_id, name, trauma)
                service.register_pasien(pasien)

                print("Registrasi Pasien Berhasil!")

            elif choice == "2":
                pasien = service.list_pasien()
                for s in pasien:
                    print(s.get_info())

            elif choice == "3":
                print("GoodBye!")
                break

            else:
                print("Opsi Tidak ada")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()