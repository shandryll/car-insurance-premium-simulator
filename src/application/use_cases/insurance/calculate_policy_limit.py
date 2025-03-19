from src.application.dto.insurance_dto import InsuranceInputDTO
from src.domain.repositories.insurance_repository import IInsuranceDomainRepository


class CalculatePolicyLimitUseCase:
    def __init__(self, insurance_repository: IInsuranceDomainRepository) -> None:
        self.__insurance_repository = insurance_repository

    def execute(self, data: InsuranceInputDTO) -> float:
        return self.__insurance_repository.calculate_policy_limit(data)
