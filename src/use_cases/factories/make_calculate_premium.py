from src.repositories.insurance.insurance_repository import IInsuranceRepository
from src.use_cases.insurance.calculate_premium import CalculatePremiumUseCase


def make_calculate_premium_use_case() -> None:
    """."""
    insurance_repository = IInsuranceRepository()
    use_case = CalculatePremiumUseCase(insurance_repository)

    return use_case
