from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-enumeration-4-NS"


class NistschemaSvIvListGYearEnumeration4Type(Enum):
    VALUE_2029_2017_2010_1977_1990_2018_1972 = (
            XmlPeriod("2029"),
            XmlPeriod("2017"),
            XmlPeriod("2010"),
            XmlPeriod("1977"),
            XmlPeriod("1990"),
            XmlPeriod("2018"),
            XmlPeriod("1972"),
        )
    VALUE_2015_2029_1998_1997_2022_2001_2001_1985 = (
            XmlPeriod("2015"),
            XmlPeriod("2029"),
            XmlPeriod("1998"),
            XmlPeriod("1997"),
            XmlPeriod("2022"),
            XmlPeriod("2001"),
            XmlPeriod("2001"),
            XmlPeriod("1985"),
        )
    VALUE_1994_1998_2004_2003_2013_2029_2021_1986_1977 = (
            XmlPeriod("1994"),
            XmlPeriod("1998"),
            XmlPeriod("2004"),
            XmlPeriod("2003"),
            XmlPeriod("2013"),
            XmlPeriod("2029"),
            XmlPeriod("2021"),
            XmlPeriod("1986"),
            XmlPeriod("1977"),
        )
    VALUE_2029_1987_2012_2006_2007_2024_2010_1970 = (
            XmlPeriod("2029"),
            XmlPeriod("1987"),
            XmlPeriod("2012"),
            XmlPeriod("2006"),
            XmlPeriod("2007"),
            XmlPeriod("2024"),
            XmlPeriod("2010"),
            XmlPeriod("1970"),
        )
    VALUE_2020_1984_1986_2001_1977_1983_2028_2005_1999_1970 = (
            XmlPeriod("2020"),
            XmlPeriod("1984"),
            XmlPeriod("1986"),
            XmlPeriod("2001"),
            XmlPeriod("1977"),
            XmlPeriod("1983"),
            XmlPeriod("2028"),
            XmlPeriod("2005"),
            XmlPeriod("1999"),
            XmlPeriod("1970"),
        )


@dataclass
class NistschemaSvIvListGYearEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gYear-enumeration-4-NS"

    value: Optional[NistschemaSvIvListGYearEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
