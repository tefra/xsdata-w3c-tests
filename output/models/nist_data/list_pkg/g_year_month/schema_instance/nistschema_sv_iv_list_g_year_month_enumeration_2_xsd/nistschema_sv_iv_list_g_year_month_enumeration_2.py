from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-enumeration-2-NS"


class NistschemaSvIvListGYearMonthEnumeration2Type(Enum):
    VALUE_2023_01_2029_12_2009_01_1979_06_2009_05 = (
        XmlPeriod("2023-01"),
        XmlPeriod("2029-12"),
        XmlPeriod("2009-01"),
        XmlPeriod("1979-06"),
        XmlPeriod("2009-05"),
    )
    VALUE_1972_06_1970_09_2024_10_2010_10_1978_07_1990_12_1998_10_1979_12 = (
        XmlPeriod("1972-06"),
        XmlPeriod("1970-09"),
        XmlPeriod("2024-10"),
        XmlPeriod("2010-10"),
        XmlPeriod("1978-07"),
        XmlPeriod("1990-12"),
        XmlPeriod("1998-10"),
        XmlPeriod("1979-12"),
    )
    VALUE_1986_10_1982_11_1992_12_2017_08_2002_02_2011_03 = (
        XmlPeriod("1986-10"),
        XmlPeriod("1982-11"),
        XmlPeriod("1992-12"),
        XmlPeriod("2017-08"),
        XmlPeriod("2002-02"),
        XmlPeriod("2011-03"),
    )
    VALUE_1974_02_2020_12_1987_08_2021_04_2005_10_1977_04_1975_11_2012_09 = (
        XmlPeriod("1974-02"),
        XmlPeriod("2020-12"),
        XmlPeriod("1987-08"),
        XmlPeriod("2021-04"),
        XmlPeriod("2005-10"),
        XmlPeriod("1977-04"),
        XmlPeriod("1975-11"),
        XmlPeriod("2012-09"),
    )
    VALUE_2027_10_2030_07_1988_10_1980_08_2015_07_1982_04_2000_05_2004_04_2027_07 = (
        XmlPeriod("2027-10"),
        XmlPeriod("2030-07"),
        XmlPeriod("1988-10"),
        XmlPeriod("1980-08"),
        XmlPeriod("2015-07"),
        XmlPeriod("1982-04"),
        XmlPeriod("2000-05"),
        XmlPeriod("2004-04"),
        XmlPeriod("2027-07"),
    )
    VALUE_1973_01_2016_08_2028_06_1983_06_2005_03_2012_01_2003_08_1995_12_2002_08 = (
        XmlPeriod("1973-01"),
        XmlPeriod("2016-08"),
        XmlPeriod("2028-06"),
        XmlPeriod("1983-06"),
        XmlPeriod("2005-03"),
        XmlPeriod("2012-01"),
        XmlPeriod("2003-08"),
        XmlPeriod("1995-12"),
        XmlPeriod("2002-08"),
    )
    VALUE_2001_11_1971_08_1976_03_1980_12_1982_02_2001_08_2000_01_1977_07_1995_12 = (
        XmlPeriod("2001-11"),
        XmlPeriod("1971-08"),
        XmlPeriod("1976-03"),
        XmlPeriod("1980-12"),
        XmlPeriod("1982-02"),
        XmlPeriod("2001-08"),
        XmlPeriod("2000-01"),
        XmlPeriod("1977-07"),
        XmlPeriod("1995-12"),
    )
    VALUE_1991_09_1984_12_1972_12_1985_10_1999_06_1989_12_2027_03_1998_04 = (
        XmlPeriod("1991-09"),
        XmlPeriod("1984-12"),
        XmlPeriod("1972-12"),
        XmlPeriod("1985-10"),
        XmlPeriod("1999-06"),
        XmlPeriod("1989-12"),
        XmlPeriod("2027-03"),
        XmlPeriod("1998-04"),
    )
    VALUE_2008_12_2014_11_1989_03_2014_05_1996_09 = (
        XmlPeriod("2008-12"),
        XmlPeriod("2014-11"),
        XmlPeriod("1989-03"),
        XmlPeriod("2014-05"),
        XmlPeriod("1996-09"),
    )
    VALUE_2019_10_2005_11_1990_12_1974_04_2016_05_1987_05_1980_08 = (
        XmlPeriod("2019-10"),
        XmlPeriod("2005-11"),
        XmlPeriod("1990-12"),
        XmlPeriod("1974-04"),
        XmlPeriod("2016-05"),
        XmlPeriod("1987-05"),
        XmlPeriod("1980-08"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListGYearMonthEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-enumeration-2-NS"

    value: NistschemaSvIvListGYearMonthEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
