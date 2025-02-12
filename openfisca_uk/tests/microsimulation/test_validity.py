from openfisca_uk import Microsimulation
import pytest
from openfisca_uk_data import FRS

YEARS = range(2017, 2022)

baseline = Microsimulation(dataset=FRS, year=2018)


@pytest.mark.parametrize("year", YEARS)
def test_not_nan(year):
    for variable in baseline.simulation.tax_benefit_system.variables:
        assert ~baseline.calc(variable, period=year).isna().any()
