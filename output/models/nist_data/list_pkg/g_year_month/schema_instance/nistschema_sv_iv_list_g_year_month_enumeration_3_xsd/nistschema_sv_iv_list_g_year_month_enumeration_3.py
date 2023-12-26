from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-enumeration-3-NS"


class NistschemaSvIvListGYearMonthEnumeration3Type(Enum):
    VALUE_2006_11_2009_01_1979_05_1992_11_2021_06 = (
        XmlPeriod("2006-11"),
        XmlPeriod("2009-01"),
        XmlPeriod("1979-05"),
        XmlPeriod("1992-11"),
        XmlPeriod("2021-06"),
    )
    VALUE_1988_04_2018_10_2010_11_2013_11_2012_08_2019_03_2013_08_2012_07 = (
        XmlPeriod("1988-04"),
        XmlPeriod("2018-10"),
        XmlPeriod("2010-11"),
        XmlPeriod("2013-11"),
        XmlPeriod("2012-08"),
        XmlPeriod("2019-03"),
        XmlPeriod("2013-08"),
        XmlPeriod("2012-07"),
    )
    VALUE_1988_07_1991_09_1990_01_2000_10_1993_04_2017_12_2011_08_2010_10 = (
        XmlPeriod("1988-07"),
        XmlPeriod("1991-09"),
        XmlPeriod("1990-01"),
        XmlPeriod("2000-10"),
        XmlPeriod("1993-04"),
        XmlPeriod("2017-12"),
        XmlPeriod("2011-08"),
        XmlPeriod("2010-10"),
    )
    VALUE_1998_11_1978_07_1990_02_2005_06_2002_03_2025_09_1971_09_2029_06_1993_01_2018_11 = (
        XmlPeriod("1998-11"),
        XmlPeriod("1978-07"),
        XmlPeriod("1990-02"),
        XmlPeriod("2005-06"),
        XmlPeriod("2002-03"),
        XmlPeriod("2025-09"),
        XmlPeriod("1971-09"),
        XmlPeriod("2029-06"),
        XmlPeriod("1993-01"),
        XmlPeriod("2018-11"),
    )
    VALUE_1996_07_1989_07_1998_06_2001_11_1986_07_1983_08_2024_01_1977_01 = (
        XmlPeriod("1996-07"),
        XmlPeriod("1989-07"),
        XmlPeriod("1998-06"),
        XmlPeriod("2001-11"),
        XmlPeriod("1986-07"),
        XmlPeriod("1983-08"),
        XmlPeriod("2024-01"),
        XmlPeriod("1977-01"),
    )
    VALUE_2011_02_2000_07_1976_09_1971_08_1990_09_1981_02_1998_03 = (
        XmlPeriod("2011-02"),
        XmlPeriod("2000-07"),
        XmlPeriod("1976-09"),
        XmlPeriod("1971-08"),
        XmlPeriod("1990-09"),
        XmlPeriod("1981-02"),
        XmlPeriod("1998-03"),
    )


@dataclass
class NistschemaSvIvListGYearMonthEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-enumeration-3-NS"

    value: Optional[NistschemaSvIvListGYearMonthEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
