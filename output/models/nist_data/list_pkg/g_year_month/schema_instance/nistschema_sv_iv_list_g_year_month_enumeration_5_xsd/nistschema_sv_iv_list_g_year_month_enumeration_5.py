from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-enumeration-5-NS"


class NistschemaSvIvListGYearMonthEnumeration5Type(Enum):
    VALUE_2021_01_1971_07_1992_04_1999_11_2028_05 = (
        XmlPeriod("2021-01"),
        XmlPeriod("1971-07"),
        XmlPeriod("1992-04"),
        XmlPeriod("1999-11"),
        XmlPeriod("2028-05"),
    )
    VALUE_2008_06_1985_01_2018_12_1975_05_1975_06_2029_06_2017_12_2019_06 = (
        XmlPeriod("2008-06"),
        XmlPeriod("1985-01"),
        XmlPeriod("2018-12"),
        XmlPeriod("1975-05"),
        XmlPeriod("1975-06"),
        XmlPeriod("2029-06"),
        XmlPeriod("2017-12"),
        XmlPeriod("2019-06"),
    )
    VALUE_1983_01_2004_07_1980_08_1997_09_1970_06_1970_12 = (
        XmlPeriod("1983-01"),
        XmlPeriod("2004-07"),
        XmlPeriod("1980-08"),
        XmlPeriod("1997-09"),
        XmlPeriod("1970-06"),
        XmlPeriod("1970-12"),
    )
    VALUE_2025_11_2001_06_1995_03_1989_11_1979_06_1973_07_1970_03 = (
        XmlPeriod("2025-11"),
        XmlPeriod("2001-06"),
        XmlPeriod("1995-03"),
        XmlPeriod("1989-11"),
        XmlPeriod("1979-06"),
        XmlPeriod("1973-07"),
        XmlPeriod("1970-03"),
    )
    VALUE_2011_10_1986_06_2004_08_2012_05_1979_08_1987_07_1994_10_1998_10 = (
        XmlPeriod("2011-10"),
        XmlPeriod("1986-06"),
        XmlPeriod("2004-08"),
        XmlPeriod("2012-05"),
        XmlPeriod("1979-08"),
        XmlPeriod("1987-07"),
        XmlPeriod("1994-10"),
        XmlPeriod("1998-10"),
    )
    VALUE_2026_09_2025_10_2029_11_1994_11_2023_06_1972_02 = (
        XmlPeriod("2026-09"),
        XmlPeriod("2025-10"),
        XmlPeriod("2029-11"),
        XmlPeriod("1994-11"),
        XmlPeriod("2023-06"),
        XmlPeriod("1972-02"),
    )
    VALUE_2006_12_2015_01_2028_03_1971_07_2015_07_2016_10_2018_11_1993_08_2021_02 = (
        XmlPeriod("2006-12"),
        XmlPeriod("2015-01"),
        XmlPeriod("2028-03"),
        XmlPeriod("1971-07"),
        XmlPeriod("2015-07"),
        XmlPeriod("2016-10"),
        XmlPeriod("2018-11"),
        XmlPeriod("1993-08"),
        XmlPeriod("2021-02"),
    )
    VALUE_2002_10_1974_11_2020_11_1982_02_2025_10_1970_11_2011_03_1996_08 = (
        XmlPeriod("2002-10"),
        XmlPeriod("1974-11"),
        XmlPeriod("2020-11"),
        XmlPeriod("1982-02"),
        XmlPeriod("2025-10"),
        XmlPeriod("1970-11"),
        XmlPeriod("2011-03"),
        XmlPeriod("1996-08"),
    )
    VALUE_2007_04_1982_04_2007_11_2013_06_2015_06_2007_05 = (
        XmlPeriod("2007-04"),
        XmlPeriod("1982-04"),
        XmlPeriod("2007-11"),
        XmlPeriod("2013-06"),
        XmlPeriod("2015-06"),
        XmlPeriod("2007-05"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListGYearMonthEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-enumeration-5-NS"

    value: NistschemaSvIvListGYearMonthEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
