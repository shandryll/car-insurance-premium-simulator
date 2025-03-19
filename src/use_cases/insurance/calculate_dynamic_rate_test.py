from src.dto.insurance_dto import InsuranceInputDTO
from src.models.address import IAddress
from src.models.car import ICar
from src.repositories.insurance.insurance_repository import IInsuranceRepository
from src.use_cases.insurance.calculate_dynamic_rate import CalculateDynamicRateUseCase


def test_it_should_be_possible_to_calculate_the_dynamic_rate() -> None:
    insurance_repository = IInsuranceRepository()
    sut = CalculateDynamicRateUseCase(insurance_repository)

    car_data = ICar(make="Toyota", model="Corolla", value=100000.0, year=2015)
    address_data = IAddress(
        street="Main Street",
        number="123",
        neighborhood="East Cost",
        city="New York",
        state="NY",
        country="USA",
        postal_code="10001",
    )

    input_data = InsuranceInputDTO(
        car=car_data,
        broker_fee=50.0,
        deductible_percentage=0.10,
        registration_location=address_data,
    )

    dynamic_rate = sut.execute(input_data)

    assert dynamic_rate == 0.10  # 10%
