from src.repositories.insurance.insurance_repository import IInsuranceRepository
from src.use_cases.insurance.calculate_dynamic_rate import CalculateDynamicRateUseCase


def make_calculate_dynamic_rate_use_case() -> None:
    """."""
    insurance_repository = IInsuranceRepository()
    use_case = CalculateDynamicRateUseCase(insurance_repository)

    return use_case
