from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-enumeration-1-NS"


class NistschemaSvIvListDateEnumeration1Type(Enum):
    VALUE_2014_04_29_1996_10_24_1981_06_13_1997_10_17_1997_09_06_1991_03_21_1987_03_24_1970_05_02_2024_06_29 = (
        XmlDate(2014, 4, 29),
        XmlDate(1996, 10, 24),
        XmlDate(1981, 6, 13),
        XmlDate(1997, 10, 17),
        XmlDate(1997, 9, 6),
        XmlDate(1991, 3, 21),
        XmlDate(1987, 3, 24),
        XmlDate(1970, 5, 2),
        XmlDate(2024, 6, 29),
    )
    VALUE_1977_04_29_2008_07_06_2028_11_03_2023_04_03_2022_08_27_2025_12_07_2001_07_21 = (
        XmlDate(1977, 4, 29),
        XmlDate(2008, 7, 6),
        XmlDate(2028, 11, 3),
        XmlDate(2023, 4, 3),
        XmlDate(2022, 8, 27),
        XmlDate(2025, 12, 7),
        XmlDate(2001, 7, 21),
    )
    VALUE_2008_09_14_2011_07_16_2017_04_12_2014_04_25_2014_01_20_1990_06_18_1983_05_09_1975_09_28_1997_07_19 = (
        XmlDate(2008, 9, 14),
        XmlDate(2011, 7, 16),
        XmlDate(2017, 4, 12),
        XmlDate(2014, 4, 25),
        XmlDate(2014, 1, 20),
        XmlDate(1990, 6, 18),
        XmlDate(1983, 5, 9),
        XmlDate(1975, 9, 28),
        XmlDate(1997, 7, 19),
    )
    VALUE_2003_09_18_2028_09_11_1997_08_15_1980_08_07_1987_12_06_2007_06_29_1971_08_27_2000_04_26_2020_07_11 = (
        XmlDate(2003, 9, 18),
        XmlDate(2028, 9, 11),
        XmlDate(1997, 8, 15),
        XmlDate(1980, 8, 7),
        XmlDate(1987, 12, 6),
        XmlDate(2007, 6, 29),
        XmlDate(1971, 8, 27),
        XmlDate(2000, 4, 26),
        XmlDate(2020, 7, 11),
    )
    VALUE_1981_10_23_1971_07_23_1999_04_16_1983_01_05_2017_12_16_2029_09_15_1985_11_29_1978_04_11_2010_04_06 = (
        XmlDate(1981, 10, 23),
        XmlDate(1971, 7, 23),
        XmlDate(1999, 4, 16),
        XmlDate(1983, 1, 5),
        XmlDate(2017, 12, 16),
        XmlDate(2029, 9, 15),
        XmlDate(1985, 11, 29),
        XmlDate(1978, 4, 11),
        XmlDate(2010, 4, 6),
    )
    VALUE_1999_05_21_1997_06_29_2010_10_08_1991_09_17_1990_10_12_2024_12_25 = (
        XmlDate(1999, 5, 21),
        XmlDate(1997, 6, 29),
        XmlDate(2010, 10, 8),
        XmlDate(1991, 9, 17),
        XmlDate(1990, 10, 12),
        XmlDate(2024, 12, 25),
    )
    VALUE_1993_05_28_2026_08_08_1972_11_19_1998_08_13_2011_10_02_2020_11_24_1996_10_13_2006_09_30 = (
        XmlDate(1993, 5, 28),
        XmlDate(2026, 8, 8),
        XmlDate(1972, 11, 19),
        XmlDate(1998, 8, 13),
        XmlDate(2011, 10, 2),
        XmlDate(2020, 11, 24),
        XmlDate(1996, 10, 13),
        XmlDate(2006, 9, 30),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListDateEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-date-enumeration-1-NS"

    value: NistschemaSvIvListDateEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
