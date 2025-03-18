from src.dto.insurance_dto import InsuranceInputDTO
from src.repositories.insurance.insurance_base_repository import IInsuranceBaseRepository


class CalculatePremiumUseCase:
    def __init__(self, insurance_repository: IInsuranceBaseRepository) -> None:
        self.__insurance_repository = insurance_repository

    def execute(self, data: InsuranceInputDTO) -> float:
        """."""
        return self.__insurance_repository.calculate_premium(data)
