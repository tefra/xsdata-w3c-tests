from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-enumeration-3-NS"


class NistschemaSvIvListGYearEnumeration3Type(Enum):
    VALUE_1997_2013_1993_1970_2004_1994_1993_1989 = (
        XmlPeriod("1997"),
        XmlPeriod("2013"),
        XmlPeriod("1993"),
        XmlPeriod("1970"),
        XmlPeriod("2004"),
        XmlPeriod("1994"),
        XmlPeriod("1993"),
        XmlPeriod("1989"),
    )
    VALUE_1980_2001_2027_1975_2014_1975_1987_2016_1982 = (
        XmlPeriod("1980"),
        XmlPeriod("2001"),
        XmlPeriod("2027"),
        XmlPeriod("1975"),
        XmlPeriod("2014"),
        XmlPeriod("1975"),
        XmlPeriod("1987"),
        XmlPeriod("2016"),
        XmlPeriod("1982"),
    )
    VALUE_2012_1986_1988_1995_1975_2001_2005 = (
        XmlPeriod("2012"),
        XmlPeriod("1986"),
        XmlPeriod("1988"),
        XmlPeriod("1995"),
        XmlPeriod("1975"),
        XmlPeriod("2001"),
        XmlPeriod("2005"),
    )
    VALUE_1989_2020_2004_2027_1977_2025_2021_1991 = (
        XmlPeriod("1989"),
        XmlPeriod("2020"),
        XmlPeriod("2004"),
        XmlPeriod("2027"),
        XmlPeriod("1977"),
        XmlPeriod("2025"),
        XmlPeriod("2021"),
        XmlPeriod("1991"),
    )
    VALUE_1975_2015_2006_2012_1982_2002 = (
        XmlPeriod("1975"),
        XmlPeriod("2015"),
        XmlPeriod("2006"),
        XmlPeriod("2012"),
        XmlPeriod("1982"),
        XmlPeriod("2002"),
    )
    VALUE_1992_1982_2024_2019_1975_2023_2020_1997_2017 = (
        XmlPeriod("1992"),
        XmlPeriod("1982"),
        XmlPeriod("2024"),
        XmlPeriod("2019"),
        XmlPeriod("1975"),
        XmlPeriod("2023"),
        XmlPeriod("2020"),
        XmlPeriod("1997"),
        XmlPeriod("2017"),
    )
    VALUE_1973_1973_2020_1992_2008_2018_2023_2015 = (
        XmlPeriod("1973"),
        XmlPeriod("1973"),
        XmlPeriod("2020"),
        XmlPeriod("1992"),
        XmlPeriod("2008"),
        XmlPeriod("2018"),
        XmlPeriod("2023"),
        XmlPeriod("2015"),
    )
    VALUE_2026_1970_2024_1990_2018_1986_1979 = (
        XmlPeriod("2026"),
        XmlPeriod("1970"),
        XmlPeriod("2024"),
        XmlPeriod("1990"),
        XmlPeriod("2018"),
        XmlPeriod("1986"),
        XmlPeriod("1979"),
    )
    VALUE_1992_1979_1974_1995_2013_1997_2015_1979_1981 = (
        XmlPeriod("1992"),
        XmlPeriod("1979"),
        XmlPeriod("1974"),
        XmlPeriod("1995"),
        XmlPeriod("2013"),
        XmlPeriod("1997"),
        XmlPeriod("2015"),
        XmlPeriod("1979"),
        XmlPeriod("1981"),
    )
    VALUE_1976_1986_1992_1972_1996_2012 = (
        XmlPeriod("1976"),
        XmlPeriod("1986"),
        XmlPeriod("1992"),
        XmlPeriod("1972"),
        XmlPeriod("1996"),
        XmlPeriod("2012"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListGYearEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-gYear-enumeration-3-NS"

    value: NistschemaSvIvListGYearEnumeration3Type = field()
