from datetime import datetime

from src.dto.insurance_dto import InsuranceInputDTO

from .insurance_base_repository import IInsuranceBaseRepository


class IInsuranceRepository(IInsuranceBaseRepository):
    def calculate_dynamic_rate(self, data: InsuranceInputDTO) -> float:
        """."""
        current_year = datetime.now().year
        car_year = data["car"]["year"]
        car_value = data["car"]["value"]

        car_year_rate = (current_year - car_year) * 0.005
        car_value_rate = (car_value // 10000) * 0.005

        dynamic_rate = car_year_rate + car_value_rate

        return dynamic_rate

    def calculate_premium(self, data: InsuranceInputDTO) -> float:
        """."""
        dynamic_rate = 0.10  # TODO: verificar se é dynamic_rate ou applied_rate
        car_value = data["car"]["value"]
        deductible_percentage = data["deductible_percentage"]
        broker_fee = data["broker_fee"]

        base_premium = car_value * dynamic_rate
        deductible_discount = base_premium * deductible_percentage
        premium = base_premium - deductible_discount + broker_fee

        return premium

    def calculate_policy_limit(self, data: InsuranceInputDTO) -> float:
        """."""
        car_value = data["car"]["value"]
        coverage_percentage = 1  # 100%
        deductible_percentage = data["deductible_percentage"]

        base_policy_limit = car_value * coverage_percentage
        deductible_value = base_policy_limit * deductible_percentage
        policy_limit = base_policy_limit - deductible_value

        return policy_limit
