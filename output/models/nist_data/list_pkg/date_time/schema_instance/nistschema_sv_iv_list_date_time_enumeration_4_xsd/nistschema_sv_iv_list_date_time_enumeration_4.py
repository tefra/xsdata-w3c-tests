from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-enumeration-4-NS"


class NistschemaSvIvListDateTimeEnumeration4Type(Enum):
    VALUE_2015_09_07_T07_48_46_2020_04_30_T13_03_39_2026_10_28_T23_06_30_2017_03_14_T01_27_36_2028_02_01_T08_59_28_1997_04_30_T17_30_56_1972_10_27_T11_47_06_1992_11_20_T16_07_04 = (
            XmlDateTime(2015, 9, 7, 7, 48, 46),
            XmlDateTime(2020, 4, 30, 13, 3, 39),
            XmlDateTime(2026, 10, 28, 23, 6, 30),
            XmlDateTime(2017, 3, 14, 1, 27, 36),
            XmlDateTime(2028, 2, 1, 8, 59, 28),
            XmlDateTime(1997, 4, 30, 17, 30, 56),
            XmlDateTime(1972, 10, 27, 11, 47, 6),
            XmlDateTime(1992, 11, 20, 16, 7, 4),
        )
    VALUE_2018_10_30_T19_20_03_1970_02_05_T08_29_16_2014_01_08_T16_08_15_2016_02_09_T17_16_22_2017_04_09_T22_49_21_1994_11_21_T10_16_46_1975_02_24_T12_48_36 = (
            XmlDateTime(2018, 10, 30, 19, 20, 3),
            XmlDateTime(1970, 2, 5, 8, 29, 16),
            XmlDateTime(2014, 1, 8, 16, 8, 15),
            XmlDateTime(2016, 2, 9, 17, 16, 22),
            XmlDateTime(2017, 4, 9, 22, 49, 21),
            XmlDateTime(1994, 11, 21, 10, 16, 46),
            XmlDateTime(1975, 2, 24, 12, 48, 36),
        )
    VALUE_2009_07_07_T22_19_51_1987_04_20_T19_51_28_1995_10_31_T19_03_31_1998_11_07_T01_47_00_2018_05_11_T12_43_48_2019_05_04_T17_43_52_2007_07_18_T21_40_02_2013_11_21_T14_55_21_1992_03_01_T15_17_08 = (
            XmlDateTime(2009, 7, 7, 22, 19, 51),
            XmlDateTime(1987, 4, 20, 19, 51, 28),
            XmlDateTime(1995, 10, 31, 19, 3, 31),
            XmlDateTime(1998, 11, 7, 1, 47, 0),
            XmlDateTime(2018, 5, 11, 12, 43, 48),
            XmlDateTime(2019, 5, 4, 17, 43, 52),
            XmlDateTime(2007, 7, 18, 21, 40, 2),
            XmlDateTime(2013, 11, 21, 14, 55, 21),
            XmlDateTime(1992, 3, 1, 15, 17, 8),
        )
    VALUE_1990_02_03_T01_57_21_2010_06_25_T11_37_03_1986_05_09_T14_53_11_1989_12_09_T11_39_13_2027_12_14_T20_45_34_1989_03_22_T00_22_50_2001_07_05_T11_57_22_2028_01_31_T22_21_32 = (
            XmlDateTime(1990, 2, 3, 1, 57, 21),
            XmlDateTime(2010, 6, 25, 11, 37, 3),
            XmlDateTime(1986, 5, 9, 14, 53, 11),
            XmlDateTime(1989, 12, 9, 11, 39, 13),
            XmlDateTime(2027, 12, 14, 20, 45, 34),
            XmlDateTime(1989, 3, 22, 0, 22, 50),
            XmlDateTime(2001, 7, 5, 11, 57, 22),
            XmlDateTime(2028, 1, 31, 22, 21, 32),
        )
    VALUE_1998_03_13_T01_24_01_2011_04_13_T08_55_42_1995_01_05_T13_16_08_2016_10_10_T05_10_57_1984_05_20_T20_07_59_2015_09_28_T22_31_45_1990_09_25_T08_34_19_1988_02_23_T05_06_40 = (
            XmlDateTime(1998, 3, 13, 1, 24, 1),
            XmlDateTime(2011, 4, 13, 8, 55, 42),
            XmlDateTime(1995, 1, 5, 13, 16, 8),
            XmlDateTime(2016, 10, 10, 5, 10, 57),
            XmlDateTime(1984, 5, 20, 20, 7, 59),
            XmlDateTime(2015, 9, 28, 22, 31, 45),
            XmlDateTime(1990, 9, 25, 8, 34, 19),
            XmlDateTime(1988, 2, 23, 5, 6, 40),
        )
    VALUE_1984_11_19_T09_36_13_1991_01_21_T07_42_14_2007_02_09_T12_55_19_1992_08_15_T19_03_22_2007_01_01_T21_30_49_1989_08_31_T02_13_52 = (
            XmlDateTime(1984, 11, 19, 9, 36, 13),
            XmlDateTime(1991, 1, 21, 7, 42, 14),
            XmlDateTime(2007, 2, 9, 12, 55, 19),
            XmlDateTime(1992, 8, 15, 19, 3, 22),
            XmlDateTime(2007, 1, 1, 21, 30, 49),
            XmlDateTime(1989, 8, 31, 2, 13, 52),
        )


@dataclass
class NistschemaSvIvListDateTimeEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-dateTime-enumeration-4-NS"

    value: Optional[NistschemaSvIvListDateTimeEnumeration4Type] = field(
        default=None
    )
