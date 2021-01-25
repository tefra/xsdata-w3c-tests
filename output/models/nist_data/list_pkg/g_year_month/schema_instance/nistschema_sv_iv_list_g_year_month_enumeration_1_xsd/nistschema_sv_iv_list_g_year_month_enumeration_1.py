from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-enumeration-1-NS"


class NistschemaSvIvListGYearMonthEnumeration1Type(Enum):
    VALUE_2019_09_1988_06_2018_06_2000_12_2007_02_1984_07_1990_07_1990_11_1980_01_1980_12 = (
            XmlPeriod("2019-09"),
            XmlPeriod("1988-06"),
            XmlPeriod("2018-06"),
            XmlPeriod("2000-12"),
            XmlPeriod("2007-02"),
            XmlPeriod("1984-07"),
            XmlPeriod("1990-07"),
            XmlPeriod("1990-11"),
            XmlPeriod("1980-01"),
            XmlPeriod("1980-12"),
        )
    VALUE_1972_04_2008_02_2010_02_2015_01_2021_01_2005_10_1972_02_1993_07 = (
            XmlPeriod("1972-04"),
            XmlPeriod("2008-02"),
            XmlPeriod("2010-02"),
            XmlPeriod("2015-01"),
            XmlPeriod("2021-01"),
            XmlPeriod("2005-10"),
            XmlPeriod("1972-02"),
            XmlPeriod("1993-07"),
        )
    VALUE_2024_11_1987_12_1971_10_2017_01_1996_07 = (
            XmlPeriod("2024-11"),
            XmlPeriod("1987-12"),
            XmlPeriod("1971-10"),
            XmlPeriod("2017-01"),
            XmlPeriod("1996-07"),
        )
    VALUE_2019_02_1988_10_1976_06_1985_03_2007_05_2026_10_1978_11_2005_10_2024_09 = (
            XmlPeriod("2019-02"),
            XmlPeriod("1988-10"),
            XmlPeriod("1976-06"),
            XmlPeriod("1985-03"),
            XmlPeriod("2007-05"),
            XmlPeriod("2026-10"),
            XmlPeriod("1978-11"),
            XmlPeriod("2005-10"),
            XmlPeriod("2024-09"),
        )
    VALUE_1989_07_1974_11_1971_12_1981_07_1990_03_2009_05_2000_12_1979_09 = (
            XmlPeriod("1989-07"),
            XmlPeriod("1974-11"),
            XmlPeriod("1971-12"),
            XmlPeriod("1981-07"),
            XmlPeriod("1990-03"),
            XmlPeriod("2009-05"),
            XmlPeriod("2000-12"),
            XmlPeriod("1979-09"),
        )
    VALUE_1990_07_1977_06_2010_02_1974_09_2026_12_1995_09 = (
            XmlPeriod("1990-07"),
            XmlPeriod("1977-06"),
            XmlPeriod("2010-02"),
            XmlPeriod("1974-09"),
            XmlPeriod("2026-12"),
            XmlPeriod("1995-09"),
        )
    VALUE_2024_11_1997_06_1991_09_2002_10_1972_12_1974_03_1976_01 = (
            XmlPeriod("2024-11"),
            XmlPeriod("1997-06"),
            XmlPeriod("1991-09"),
            XmlPeriod("2002-10"),
            XmlPeriod("1972-12"),
            XmlPeriod("1974-03"),
            XmlPeriod("1976-01"),
        )
    VALUE_1975_06_2027_07_1993_11_2025_09_1986_12_1987_02 = (
            XmlPeriod("1975-06"),
            XmlPeriod("2027-07"),
            XmlPeriod("1993-11"),
            XmlPeriod("2025-09"),
            XmlPeriod("1986-12"),
            XmlPeriod("1987-02"),
        )
    VALUE_1972_01_1972_04_1987_07_1979_05_1978_10_2016_01_2026_08_2019_09 = (
            XmlPeriod("1972-01"),
            XmlPeriod("1972-04"),
            XmlPeriod("1987-07"),
            XmlPeriod("1979-05"),
            XmlPeriod("1978-10"),
            XmlPeriod("2016-01"),
            XmlPeriod("2026-08"),
            XmlPeriod("2019-09"),
        )


@dataclass
class NistschemaSvIvListGYearMonthEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-enumeration-1-NS"

    value: Optional[NistschemaSvIvListGYearMonthEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
