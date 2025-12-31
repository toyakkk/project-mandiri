class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    def get_info(self) -> str:
        return f"User ID: {self.user_id}, Name: {self.name}"
    
class Pasien(User):
    def __init__(self, user_id: int, name: str, trauma_type: str):
        super().__init__(user_id, name)
        self.trauma_type = trauma_type

    def get_info(self) -> str:
        return (
            f"Pasien ID: {self.user_id}, "
            f"Name: {self.name}, "
            f"Trauma Type: {self.trauma_type}"
        )
    


pasien = Pasien(1, "toya", "trauma emosional")
print(pasien.get_info())