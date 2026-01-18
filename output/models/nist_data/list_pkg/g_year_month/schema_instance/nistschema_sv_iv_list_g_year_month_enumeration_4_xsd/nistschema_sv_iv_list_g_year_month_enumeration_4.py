from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-enumeration-4-NS"


class NistschemaSvIvListGYearMonthEnumeration4Type(Enum):
    VALUE_1995_11_1972_02_2014_02_1980_07_1972_03_2000_03 = (
        XmlPeriod("1995-11"),
        XmlPeriod("1972-02"),
        XmlPeriod("2014-02"),
        XmlPeriod("1980-07"),
        XmlPeriod("1972-03"),
        XmlPeriod("2000-03"),
    )
    VALUE_2026_09_1980_01_1999_12_1976_04_1997_10 = (
        XmlPeriod("2026-09"),
        XmlPeriod("1980-01"),
        XmlPeriod("1999-12"),
        XmlPeriod("1976-04"),
        XmlPeriod("1997-10"),
    )
    VALUE_1985_03_2025_03_2007_11_1980_04_2021_02_2029_03_2002_03_1971_11_1988_09 = (
        XmlPeriod("1985-03"),
        XmlPeriod("2025-03"),
        XmlPeriod("2007-11"),
        XmlPeriod("1980-04"),
        XmlPeriod("2021-02"),
        XmlPeriod("2029-03"),
        XmlPeriod("2002-03"),
        XmlPeriod("1971-11"),
        XmlPeriod("1988-09"),
    )
    VALUE_1994_06_2026_10_2015_04_1972_10_2030_11_2000_02_1980_10_1983_11 = (
        XmlPeriod("1994-06"),
        XmlPeriod("2026-10"),
        XmlPeriod("2015-04"),
        XmlPeriod("1972-10"),
        XmlPeriod("2030-11"),
        XmlPeriod("2000-02"),
        XmlPeriod("1980-10"),
        XmlPeriod("1983-11"),
    )
    VALUE_1979_10_2021_04_1980_04_1979_06_1973_11_2029_06_1983_10_1996_12_2023_05 = (
        XmlPeriod("1979-10"),
        XmlPeriod("2021-04"),
        XmlPeriod("1980-04"),
        XmlPeriod("1979-06"),
        XmlPeriod("1973-11"),
        XmlPeriod("2029-06"),
        XmlPeriod("1983-10"),
        XmlPeriod("1996-12"),
        XmlPeriod("2023-05"),
    )
    VALUE_2006_03_2019_08_1974_02_2025_03_1990_06_2004_05_1974_10_2030_04_1982_07 = (
        XmlPeriod("2006-03"),
        XmlPeriod("2019-08"),
        XmlPeriod("1974-02"),
        XmlPeriod("2025-03"),
        XmlPeriod("1990-06"),
        XmlPeriod("2004-05"),
        XmlPeriod("1974-10"),
        XmlPeriod("2030-04"),
        XmlPeriod("1982-07"),
    )
    VALUE_2015_11_1987_06_2005_02_1997_10_2016_01_2015_02_2019_09_1992_07 = (
        XmlPeriod("2015-11"),
        XmlPeriod("1987-06"),
        XmlPeriod("2005-02"),
        XmlPeriod("1997-10"),
        XmlPeriod("2016-01"),
        XmlPeriod("2015-02"),
        XmlPeriod("2019-09"),
        XmlPeriod("1992-07"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListGYearMonthEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-enumeration-4-NS"

    value: NistschemaSvIvListGYearMonthEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
