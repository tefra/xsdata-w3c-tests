from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-enumeration-5-NS"


class NistschemaSvIvListDateEnumeration5Type(Enum):
    VALUE_2004_03_18_1982_03_29_1991_07_13_1998_06_30_1992_03_20_2017_10_12 = (
            XmlDate(2004, 3, 18),
            XmlDate(1982, 3, 29),
            XmlDate(1991, 7, 13),
            XmlDate(1998, 6, 30),
            XmlDate(1992, 3, 20),
            XmlDate(2017, 10, 12),
        )
    VALUE_1974_05_03_1977_04_21_2014_12_12_1982_11_23_2025_06_26_1997_09_03_1988_06_24_2021_05_11 = (
            XmlDate(1974, 5, 3),
            XmlDate(1977, 4, 21),
            XmlDate(2014, 12, 12),
            XmlDate(1982, 11, 23),
            XmlDate(2025, 6, 26),
            XmlDate(1997, 9, 3),
            XmlDate(1988, 6, 24),
            XmlDate(2021, 5, 11),
        )
    VALUE_1987_11_18_1974_05_19_2008_11_11_1990_07_03_1994_03_11_1998_01_15 = (
            XmlDate(1987, 11, 18),
            XmlDate(1974, 5, 19),
            XmlDate(2008, 11, 11),
            XmlDate(1990, 7, 3),
            XmlDate(1994, 3, 11),
            XmlDate(1998, 1, 15),
        )
    VALUE_1990_11_17_1977_03_24_1993_09_27_2022_10_16_2008_05_09_1980_12_07_1981_05_24_2023_01_01_1993_09_21 = (
            XmlDate(1990, 11, 17),
            XmlDate(1977, 3, 24),
            XmlDate(1993, 9, 27),
            XmlDate(2022, 10, 16),
            XmlDate(2008, 5, 9),
            XmlDate(1980, 12, 7),
            XmlDate(1981, 5, 24),
            XmlDate(2023, 1, 1),
            XmlDate(1993, 9, 21),
        )
    VALUE_2006_03_10_2014_03_09_2030_04_19_1981_10_08_2004_08_07_1996_04_20_1979_11_10 = (
            XmlDate(2006, 3, 10),
            XmlDate(2014, 3, 9),
            XmlDate(2030, 4, 19),
            XmlDate(1981, 10, 8),
            XmlDate(2004, 8, 7),
            XmlDate(1996, 4, 20),
            XmlDate(1979, 11, 10),
        )
    VALUE_1985_08_18_2017_08_19_2002_06_13_2027_10_07_1976_06_28_2010_08_28 = (
            XmlDate(1985, 8, 18),
            XmlDate(2017, 8, 19),
            XmlDate(2002, 6, 13),
            XmlDate(2027, 10, 7),
            XmlDate(1976, 6, 28),
            XmlDate(2010, 8, 28),
        )


@dataclass
class NistschemaSvIvListDateEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-date-enumeration-5-NS"

    value: Optional[NistschemaSvIvListDateEnumeration5Type] = field(
        default=None
    )
