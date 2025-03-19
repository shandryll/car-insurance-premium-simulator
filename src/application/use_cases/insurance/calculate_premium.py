from src.application.dto.insurance_dto import InsuranceInputDTO
from src.domain.repositories.insurance_repository import IInsuranceDomainRepository


class CalculatePremiumUseCase:
    def __init__(self, insurance_repository: IInsuranceDomainRepository) -> None:
        self.__insurance_repository = insurance_repository

    def execute(self, data: InsuranceInputDTO, applied_rate: float) -> float:
        return self.__insurance_repository.calculate_premium(data, applied_rate)
