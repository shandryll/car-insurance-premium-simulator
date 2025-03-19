from abc import ABC, abstractmethod

from src.application.dto.insurance_dto import InsuranceInputDTO


class IInsuranceDomainRepository(ABC):
    @abstractmethod
    def calculate_dynamic_rate(self, data: InsuranceInputDTO) -> float:
        pass

    @abstractmethod
    def calculate_premium(self, data: InsuranceInputDTO, applied_rate: float) -> float:
        pass

    @abstractmethod
    def calculate_policy_limit(self, data: InsuranceInputDTO) -> float:
        pass
