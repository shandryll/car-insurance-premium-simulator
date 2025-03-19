from src.repositories.insurance.insurance_repository import IInsuranceRepository
from src.use_cases.insurance.calculate_policy_limit import CalculatePolicyLimitUseCase


def make_calculate_policy_limit_use_case() -> None:
    insurance_repository = IInsuranceRepository()
    use_case = CalculatePolicyLimitUseCase(insurance_repository)

    return use_case
