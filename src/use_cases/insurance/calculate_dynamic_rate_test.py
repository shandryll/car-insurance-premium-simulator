from src.repositories.insurance.insurance_repository import IInsuranceRepository
from src.use_cases.insurance.calculate_dynamic_rate import CalculateDynamicRateUseCase


def test_it_should_be_possible_to_calculate_the_dynamic_rate() -> None:
    """."""
    insurance_repository = IInsuranceRepository()
    sut = CalculateDynamicRateUseCase(insurance_repository)

    input_data = {
        "car": {
            "make": "Toyota",
            "model": "Corolla",
            "year": 2015,
            "value": 100000.0,
        },
        "deductible_percentage": 0.10,
        "broker_fee": 50.0,
        "registration_location": {
            "street": "Main Street",
            "number": "123",
            "city": "New York",
            "state": "NY",
            "country": "USA",
            "postal_code": "10001",
        },
    }

    dynamic_rate = sut.execute(input_data)

    assert dynamic_rate == 0.10  # 10%
