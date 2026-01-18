from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-enumeration-1-NS"


class NistschemaSvIvListGYearEnumeration1Type(Enum):
    VALUE_2029_1976_2001_1970_2028_1974_2025_2027_1986 = (
        XmlPeriod("2029"),
        XmlPeriod("1976"),
        XmlPeriod("2001"),
        XmlPeriod("1970"),
        XmlPeriod("2028"),
        XmlPeriod("1974"),
        XmlPeriod("2025"),
        XmlPeriod("2027"),
        XmlPeriod("1986"),
    )
    VALUE_1987_1994_1987_2017_2029_1985 = (
        XmlPeriod("1987"),
        XmlPeriod("1994"),
        XmlPeriod("1987"),
        XmlPeriod("2017"),
        XmlPeriod("2029"),
        XmlPeriod("1985"),
    )
    VALUE_2003_2004_2009_1986_1979 = (
        XmlPeriod("2003"),
        XmlPeriod("2004"),
        XmlPeriod("2009"),
        XmlPeriod("1986"),
        XmlPeriod("1979"),
    )
    VALUE_2024_2010_2016_2024_2020_2026 = (
        XmlPeriod("2024"),
        XmlPeriod("2010"),
        XmlPeriod("2016"),
        XmlPeriod("2024"),
        XmlPeriod("2020"),
        XmlPeriod("2026"),
    )
    VALUE_2004_2016_2009_1973_2027_1981_1982_2023 = (
        XmlPeriod("2004"),
        XmlPeriod("2016"),
        XmlPeriod("2009"),
        XmlPeriod("1973"),
        XmlPeriod("2027"),
        XmlPeriod("1981"),
        XmlPeriod("1982"),
        XmlPeriod("2023"),
    )
    VALUE_2028_2013_1980_2019_2024_2013_2009 = (
        XmlPeriod("2028"),
        XmlPeriod("2013"),
        XmlPeriod("1980"),
        XmlPeriod("2019"),
        XmlPeriod("2024"),
        XmlPeriod("2013"),
        XmlPeriod("2009"),
    )
    VALUE_2001_1979_1996_2004_2011_2029_2011 = (
        XmlPeriod("2001"),
        XmlPeriod("1979"),
        XmlPeriod("1996"),
        XmlPeriod("2004"),
        XmlPeriod("2011"),
        XmlPeriod("2029"),
        XmlPeriod("2011"),
    )
    VALUE_2000_2026_1988_2009_1971_2008_2001 = (
        XmlPeriod("2000"),
        XmlPeriod("2026"),
        XmlPeriod("1988"),
        XmlPeriod("2009"),
        XmlPeriod("1971"),
        XmlPeriod("2008"),
        XmlPeriod("2001"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListGYearEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-gYear-enumeration-1-NS"

    value: NistschemaSvIvListGYearEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
