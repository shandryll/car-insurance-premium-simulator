from src.application.use_cases.insurance.calculate_dynamic_rate import CalculateDynamicRateUseCase
from src.infrastructure.repositories.insurance_repository import IInsuranceRepository


def make_calculate_dynamic_rate_use_case() -> None:
    insurance_repository = IInsuranceRepository()
    use_case = CalculateDynamicRateUseCase(insurance_repository)

    return use_case
