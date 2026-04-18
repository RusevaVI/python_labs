from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass


class Rentable(ABC):
    @abstractmethod
    def calculate_access_cost(self, days: int) -> float:
        pass