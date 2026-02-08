from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-enumeration-4-NS"


class NistschemaSvIvListDateEnumeration4Type(Enum):
    VALUE_1975_08_07_1986_06_10_2015_09_26_1975_11_10_1975_05_12_2004_04_28_2001_01_24_2030_08_12 = (
        XmlDate(1975, 8, 7),
        XmlDate(1986, 6, 10),
        XmlDate(2015, 9, 26),
        XmlDate(1975, 11, 10),
        XmlDate(1975, 5, 12),
        XmlDate(2004, 4, 28),
        XmlDate(2001, 1, 24),
        XmlDate(2030, 8, 12),
    )
    VALUE_1997_11_23_1998_10_26_1982_05_22_2028_02_02_2008_03_14_1983_04_08_1999_08_24_1989_10_10_2003_07_25_2001_09_22 = (
        XmlDate(1997, 11, 23),
        XmlDate(1998, 10, 26),
        XmlDate(1982, 5, 22),
        XmlDate(2028, 2, 2),
        XmlDate(2008, 3, 14),
        XmlDate(1983, 4, 8),
        XmlDate(1999, 8, 24),
        XmlDate(1989, 10, 10),
        XmlDate(2003, 7, 25),
        XmlDate(2001, 9, 22),
    )
    VALUE_2019_06_09_2010_12_25_2008_07_03_2001_05_11_1971_07_13_1985_11_13 = (
        XmlDate(2019, 6, 9),
        XmlDate(2010, 12, 25),
        XmlDate(2008, 7, 3),
        XmlDate(2001, 5, 11),
        XmlDate(1971, 7, 13),
        XmlDate(1985, 11, 13),
    )
    VALUE_2017_02_03_1994_10_09_2019_12_12_1984_08_02_1992_11_15_1986_03_17_2027_12_31_2021_12_16 = (
        XmlDate(2017, 2, 3),
        XmlDate(1994, 10, 9),
        XmlDate(2019, 12, 12),
        XmlDate(1984, 8, 2),
        XmlDate(1992, 11, 15),
        XmlDate(1986, 3, 17),
        XmlDate(2027, 12, 31),
        XmlDate(2021, 12, 16),
    )
    VALUE_1979_04_21_2020_01_17_1993_09_19_1992_01_14_1975_09_18_2015_05_03_2014_04_29_2005_06_15_2004_09_27_2029_08_15 = (
        XmlDate(1979, 4, 21),
        XmlDate(2020, 1, 17),
        XmlDate(1993, 9, 19),
        XmlDate(1992, 1, 14),
        XmlDate(1975, 9, 18),
        XmlDate(2015, 5, 3),
        XmlDate(2014, 4, 29),
        XmlDate(2005, 6, 15),
        XmlDate(2004, 9, 27),
        XmlDate(2029, 8, 15),
    )
    VALUE_1999_07_19_1986_03_26_1999_12_27_1972_05_16_1987_09_16_2015_09_17 = (
        XmlDate(1999, 7, 19),
        XmlDate(1986, 3, 26),
        XmlDate(1999, 12, 27),
        XmlDate(1972, 5, 16),
        XmlDate(1987, 9, 16),
        XmlDate(2015, 9, 17),
    )
    VALUE_2010_07_09_1977_06_28_1982_10_24_1986_10_13_1986_09_10_2024_12_10_1990_09_11 = (
        XmlDate(2010, 7, 9),
        XmlDate(1977, 6, 28),
        XmlDate(1982, 10, 24),
        XmlDate(1986, 10, 13),
        XmlDate(1986, 9, 10),
        XmlDate(2024, 12, 10),
        XmlDate(1990, 9, 11),
    )
    VALUE_2023_10_14_1980_10_09_1982_12_05_1988_04_09_1984_02_11_2021_05_24_2017_07_12 = (
        XmlDate(2023, 10, 14),
        XmlDate(1980, 10, 9),
        XmlDate(1982, 12, 5),
        XmlDate(1988, 4, 9),
        XmlDate(1984, 2, 11),
        XmlDate(2021, 5, 24),
        XmlDate(2017, 7, 12),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListDateEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-date-enumeration-4-NS"

    value: NistschemaSvIvListDateEnumeration4Type = field()
