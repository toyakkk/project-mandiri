from abc import ABC, abstractmethod
from models.users import Pasien


class PasienRepository(ABC):
    @abstractmethod
    def add(self, pasien: Pasien):
        pass

    @abstractmethod
    def get_all(self):
        pass


class InMemoryPasienRepository(PasienRepository):
    def __init__(self):
        self._pasien = []

    def add(self, pasien: Pasien):
        self._pasien.append(pasien)

    def get_all(self):
        return self._pasien