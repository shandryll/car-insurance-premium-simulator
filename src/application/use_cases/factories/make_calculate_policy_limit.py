from src.application.use_cases.insurance.calculate_policy_limit import CalculatePolicyLimitUseCase
from src.infrastructure.repositories.insurance_repository import IInsuranceRepository


def make_calculate_policy_limit_use_case() -> None:
    insurance_repository = IInsuranceRepository()
    use_case = CalculatePolicyLimitUseCase(insurance_repository)

    return use_case
