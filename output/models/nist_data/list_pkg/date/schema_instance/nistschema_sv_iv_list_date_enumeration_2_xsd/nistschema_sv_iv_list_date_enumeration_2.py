from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-enumeration-2-NS"


class NistschemaSvIvListDateEnumeration2Type(Enum):
    VALUE_2024_09_15_2013_11_23_1989_04_09_2001_10_10_1978_05_08_1980_09_07_1970_11_26_2015_03_09 = (
            XmlDate(2024, 9, 15),
            XmlDate(2013, 11, 23),
            XmlDate(1989, 4, 9),
            XmlDate(2001, 10, 10),
            XmlDate(1978, 5, 8),
            XmlDate(1980, 9, 7),
            XmlDate(1970, 11, 26),
            XmlDate(2015, 3, 9),
        )
    VALUE_1975_06_30_2011_01_23_1971_02_24_2028_08_01_2017_11_02 = (
            XmlDate(1975, 6, 30),
            XmlDate(2011, 1, 23),
            XmlDate(1971, 2, 24),
            XmlDate(2028, 8, 1),
            XmlDate(2017, 11, 2),
        )
    VALUE_2028_06_06_2007_09_15_2003_12_06_1995_10_27_2016_03_21_2012_05_18_2008_12_08_2030_09_22_2005_11_01 = (
            XmlDate(2028, 6, 6),
            XmlDate(2007, 9, 15),
            XmlDate(2003, 12, 6),
            XmlDate(1995, 10, 27),
            XmlDate(2016, 3, 21),
            XmlDate(2012, 5, 18),
            XmlDate(2008, 12, 8),
            XmlDate(2030, 9, 22),
            XmlDate(2005, 11, 1),
        )
    VALUE_2019_11_18_1989_04_08_1993_12_11_2003_08_19_2017_07_29_2030_11_20_1985_06_02_2007_12_17_2013_01_10 = (
            XmlDate(2019, 11, 18),
            XmlDate(1989, 4, 8),
            XmlDate(1993, 12, 11),
            XmlDate(2003, 8, 19),
            XmlDate(2017, 7, 29),
            XmlDate(2030, 11, 20),
            XmlDate(1985, 6, 2),
            XmlDate(2007, 12, 17),
            XmlDate(2013, 1, 10),
        )
    VALUE_1982_12_14_2029_06_02_1971_11_02_2018_02_05_2013_03_31_1978_05_29 = (
            XmlDate(1982, 12, 14),
            XmlDate(2029, 6, 2),
            XmlDate(1971, 11, 2),
            XmlDate(2018, 2, 5),
            XmlDate(2013, 3, 31),
            XmlDate(1978, 5, 29),
        )
    VALUE_1972_04_12_1991_01_10_2014_03_22_1992_10_21_2028_10_04_2016_05_27_1990_11_15_2022_11_04 = (
            XmlDate(1972, 4, 12),
            XmlDate(1991, 1, 10),
            XmlDate(2014, 3, 22),
            XmlDate(1992, 10, 21),
            XmlDate(2028, 10, 4),
            XmlDate(2016, 5, 27),
            XmlDate(1990, 11, 15),
            XmlDate(2022, 11, 4),
        )


@dataclass
class NistschemaSvIvListDateEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-date-enumeration-2-NS"

    value: Optional[NistschemaSvIvListDateEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
