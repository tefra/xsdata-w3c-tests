from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-enumeration-2-NS"


class NistschemaSvIvListGYearEnumeration2Type(Enum):
    VALUE_2020_2006_1971_1986_1975_1984 = (
            XmlPeriod("2020"),
            XmlPeriod("2006"),
            XmlPeriod("1971"),
            XmlPeriod("1986"),
            XmlPeriod("1975"),
            XmlPeriod("1984"),
        )
    VALUE_2029_1983_1986_2015_2017_2004_2010_2021_1978_2008 = (
            XmlPeriod("2029"),
            XmlPeriod("1983"),
            XmlPeriod("1986"),
            XmlPeriod("2015"),
            XmlPeriod("2017"),
            XmlPeriod("2004"),
            XmlPeriod("2010"),
            XmlPeriod("2021"),
            XmlPeriod("1978"),
            XmlPeriod("2008"),
        )
    VALUE_1999_1993_1995_1996_1983_1983_1975_2019_1989 = (
            XmlPeriod("1999"),
            XmlPeriod("1993"),
            XmlPeriod("1995"),
            XmlPeriod("1996"),
            XmlPeriod("1983"),
            XmlPeriod("1983"),
            XmlPeriod("1975"),
            XmlPeriod("2019"),
            XmlPeriod("1989"),
        )
    VALUE_1972_1988_2021_2014_2007_2012_2005 = (
            XmlPeriod("1972"),
            XmlPeriod("1988"),
            XmlPeriod("2021"),
            XmlPeriod("2014"),
            XmlPeriod("2007"),
            XmlPeriod("2012"),
            XmlPeriod("2005"),
        )
    VALUE_1970_2023_1975_2019_2024_2019_2021_2001 = (
            XmlPeriod("1970"),
            XmlPeriod("2023"),
            XmlPeriod("1975"),
            XmlPeriod("2019"),
            XmlPeriod("2024"),
            XmlPeriod("2019"),
            XmlPeriod("2021"),
            XmlPeriod("2001"),
        )
    VALUE_1994_2005_1998_2005_2029_1970_2017 = (
            XmlPeriod("1994"),
            XmlPeriod("2005"),
            XmlPeriod("1998"),
            XmlPeriod("2005"),
            XmlPeriod("2029"),
            XmlPeriod("1970"),
            XmlPeriod("2017"),
        )
    VALUE_1989_2009_1989_2014_1989_1991_1985_1984 = (
            XmlPeriod("1989"),
            XmlPeriod("2009"),
            XmlPeriod("1989"),
            XmlPeriod("2014"),
            XmlPeriod("1989"),
            XmlPeriod("1991"),
            XmlPeriod("1985"),
            XmlPeriod("1984"),
        )


@dataclass
class NistschemaSvIvListGYearEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-gYear-enumeration-2-NS"

    value: Optional[NistschemaSvIvListGYearEnumeration2Type] = field(
        default=None
    )
