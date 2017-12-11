"""
Tests for lookups of elemental data
"""

from bse import lut
import pytest

def test_lut():

    for Z in range(100):
        data = lut.element_data_from_Z(Z)
        assert data[0] == Z

        assert data == lut.element_data_from_sym(data[1])
        assert data == lut.element_data_from_name(data[2])

        assert data[1] == lut.element_sym_from_Z(Z)
        assert data[2] == lut.element_name_from_Z(Z)

        nsym = lut.normalize_element_symbol(data[1])
        nname = lut.normalize_element_name(data[2])

        assert nsym[0] == data[1][0].upper()
        assert nname[0] == data[2][0].upper()


    for am in range(12):
        s = lut.amint_to_char([am])
        assert am == lut.amchar_to_int(s)[0]

        combined = list(range(am+1))
        s = lut.amint_to_char(combined)
        assert combined == lut.amchar_to_int(s)