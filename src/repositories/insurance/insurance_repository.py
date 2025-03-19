from datetime import datetime

from src.dto.insurance_dto import InsuranceInputDTO
from src.utils.handler import monetary_handler

from .insurance_base_repository import IInsuranceBaseRepository


class IInsuranceRepository(IInsuranceBaseRepository):
    def calculate_dynamic_rate(self, data: InsuranceInputDTO) -> float:
        insurance_input = data.model_dump()

        current_year = datetime.now().year
        car_year = insurance_input["car"]["year"]
        car_value = insurance_input["car"]["value"]

        car_year_rate = (current_year - car_year) * 0.005
        car_value_rate = (car_value // 10000) * 0.005

        dynamic_rate = car_year_rate + car_value_rate

        return dynamic_rate

    def calculate_premium(self, data: InsuranceInputDTO, applied_rate: float) -> float:
        insurance_input = data.model_dump()

        car_value = insurance_input["car"]["value"]
        deductible_percentage = insurance_input["deductible_percentage"]
        broker_fee = insurance_input["broker_fee"]

        base_premium = car_value * applied_rate
        deductible_discount = base_premium * deductible_percentage
        premium = monetary_handler(base_premium - deductible_discount + broker_fee)

        return premium

    def calculate_policy_limit(self, data: InsuranceInputDTO) -> dict[str, float]:
        insurance_input = data.model_dump()

        car_value = insurance_input["car"]["value"]
        coverage_percentage = 1  # 100%
        deductible_percentage = insurance_input["deductible_percentage"]

        base_policy_limit = car_value * coverage_percentage
        deductible_value = monetary_handler(base_policy_limit * deductible_percentage)
        policy_limit = monetary_handler(base_policy_limit - deductible_value)

        return {
            "policy_limit": policy_limit,
            "deductible_value": deductible_value,
        }
