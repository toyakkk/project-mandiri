from repositories.pasien_repo import PasienRepository
from utils.logger import AppLogger


class CounselingService:
    def __init__(self, repository: PasienRepository):
        self.repository = repository
        self.logger = AppLogger.get_logger()

    def register_pasien(self, pasien):
        self.repository.add(pasien)
        self.logger.info(f"Pasien registered: {pasien.name}")

    def list_pasien(self):
        self.logger.info("Listing all pasien")
        return self.repository.get_all()
