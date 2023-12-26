from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-enumeration-5-NS"


class NistschemaSvIvListGYearEnumeration5Type(Enum):
    VALUE_2007_2010_2018_1982_1984_2024 = (
        XmlPeriod("2007"),
        XmlPeriod("2010"),
        XmlPeriod("2018"),
        XmlPeriod("1982"),
        XmlPeriod("1984"),
        XmlPeriod("2024"),
    )
    VALUE_2026_1979_2011_2014_1994_2023 = (
        XmlPeriod("2026"),
        XmlPeriod("1979"),
        XmlPeriod("2011"),
        XmlPeriod("2014"),
        XmlPeriod("1994"),
        XmlPeriod("2023"),
    )
    VALUE_2013_2007_1991_2011_2027_1971_1974_2029 = (
        XmlPeriod("2013"),
        XmlPeriod("2007"),
        XmlPeriod("1991"),
        XmlPeriod("2011"),
        XmlPeriod("2027"),
        XmlPeriod("1971"),
        XmlPeriod("1974"),
        XmlPeriod("2029"),
    )
    VALUE_2006_1970_1996_1993_2021 = (
        XmlPeriod("2006"),
        XmlPeriod("1970"),
        XmlPeriod("1996"),
        XmlPeriod("1993"),
        XmlPeriod("2021"),
    )
    VALUE_1991_2018_1974_1989_2011_1987_1989_1998_1992 = (
        XmlPeriod("1991"),
        XmlPeriod("2018"),
        XmlPeriod("1974"),
        XmlPeriod("1989"),
        XmlPeriod("2011"),
        XmlPeriod("1987"),
        XmlPeriod("1989"),
        XmlPeriod("1998"),
        XmlPeriod("1992"),
    )


@dataclass
class NistschemaSvIvListGYearEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-gYear-enumeration-5-NS"

    value: Optional[NistschemaSvIvListGYearEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
