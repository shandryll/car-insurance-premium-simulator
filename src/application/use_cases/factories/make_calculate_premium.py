from src.application.use_cases.insurance.calculate_premium import CalculatePremiumUseCase
from src.infrastructure.repositories.insurance_repository import IInsuranceRepository


def make_calculate_premium_use_case() -> None:
    insurance_repository = IInsuranceRepository()
    use_case = CalculatePremiumUseCase(insurance_repository)

    return use_case
