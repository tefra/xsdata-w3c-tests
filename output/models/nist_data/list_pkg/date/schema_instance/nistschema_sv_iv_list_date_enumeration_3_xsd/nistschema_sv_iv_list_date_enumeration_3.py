from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-enumeration-3-NS"


class NistschemaSvIvListDateEnumeration3Type(Enum):
    VALUE_2005_06_20_2009_08_24_1994_01_13_1971_03_22_2012_09_21_2000_02_24_2010_10_07_2012_07_07_1983_12_24 = (
        XmlDate(2005, 6, 20),
        XmlDate(2009, 8, 24),
        XmlDate(1994, 1, 13),
        XmlDate(1971, 3, 22),
        XmlDate(2012, 9, 21),
        XmlDate(2000, 2, 24),
        XmlDate(2010, 10, 7),
        XmlDate(2012, 7, 7),
        XmlDate(1983, 12, 24),
    )
    VALUE_2025_09_07_1996_03_19_1971_02_18_2001_03_25_1975_09_11_1976_02_13_1980_12_10_1972_08_21 = (
        XmlDate(2025, 9, 7),
        XmlDate(1996, 3, 19),
        XmlDate(1971, 2, 18),
        XmlDate(2001, 3, 25),
        XmlDate(1975, 9, 11),
        XmlDate(1976, 2, 13),
        XmlDate(1980, 12, 10),
        XmlDate(1972, 8, 21),
    )
    VALUE_2014_07_06_2028_02_01_1990_05_05_1979_10_27_1998_09_05_2018_07_19 = (
        XmlDate(2014, 7, 6),
        XmlDate(2028, 2, 1),
        XmlDate(1990, 5, 5),
        XmlDate(1979, 10, 27),
        XmlDate(1998, 9, 5),
        XmlDate(2018, 7, 19),
    )
    VALUE_2003_07_21_1987_08_20_2023_12_02_2004_12_20_2013_01_28_2005_02_23_2016_06_07_2013_12_27 = (
        XmlDate(2003, 7, 21),
        XmlDate(1987, 8, 20),
        XmlDate(2023, 12, 2),
        XmlDate(2004, 12, 20),
        XmlDate(2013, 1, 28),
        XmlDate(2005, 2, 23),
        XmlDate(2016, 6, 7),
        XmlDate(2013, 12, 27),
    )
    VALUE_2029_12_12_1977_08_04_1973_04_04_1980_03_26_1987_12_28_2004_07_10_1999_01_23 = (
        XmlDate(2029, 12, 12),
        XmlDate(1977, 8, 4),
        XmlDate(1973, 4, 4),
        XmlDate(1980, 3, 26),
        XmlDate(1987, 12, 28),
        XmlDate(2004, 7, 10),
        XmlDate(1999, 1, 23),
    )
    VALUE_1972_04_02_2009_06_22_2012_12_31_2018_09_01_2018_12_09_2021_12_11_1975_05_11 = (
        XmlDate(1972, 4, 2),
        XmlDate(2009, 6, 22),
        XmlDate(2012, 12, 31),
        XmlDate(2018, 9, 1),
        XmlDate(2018, 12, 9),
        XmlDate(2021, 12, 11),
        XmlDate(1975, 5, 11),
    )
    VALUE_1971_02_24_2019_06_15_1991_08_21_2029_12_24_2029_01_13 = (
        XmlDate(1971, 2, 24),
        XmlDate(2019, 6, 15),
        XmlDate(1991, 8, 21),
        XmlDate(2029, 12, 24),
        XmlDate(2029, 1, 13),
    )
    VALUE_1970_02_18_2005_05_25_1994_04_09_2017_06_27_2008_08_24_2012_07_08_1970_01_26_1978_01_22 = (
        XmlDate(1970, 2, 18),
        XmlDate(2005, 5, 25),
        XmlDate(1994, 4, 9),
        XmlDate(2017, 6, 27),
        XmlDate(2008, 8, 24),
        XmlDate(2012, 7, 8),
        XmlDate(1970, 1, 26),
        XmlDate(1978, 1, 22),
    )
    VALUE_1988_03_08_1991_07_04_2006_01_08_2000_04_02_1991_05_08 = (
        XmlDate(1988, 3, 8),
        XmlDate(1991, 7, 4),
        XmlDate(2006, 1, 8),
        XmlDate(2000, 4, 2),
        XmlDate(1991, 5, 8),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListDateEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-date-enumeration-3-NS"

    value: NistschemaSvIvListDateEnumeration3Type = field()
