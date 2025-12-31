import unittest
from models.users import Pasien
from repositories.pasien_repo import InMemoryPasienRepository
from services.counseling import CounselingService


class TestCounselingService(unittest.TestCase):
    def test_register_pasien(self):
        repo = InMemoryPasienRepository()
        service = CounselingService(repo)

        pasien = Pasien(1, "Test user", "Trauma test")
        service.register_pasien(pasien)

        self.assertEqual(len(repo.get_all()), 1)


if __name__ == "__main__":
    unittest.main()