from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-enumeration-5-NS"


class NistschemaSvIvListGYearEnumeration5Type(Enum):
    """
    :cvar VALUE_2007_2010_2018_1982_1984_2024:
    :cvar VALUE_2026_1979_2011_2014_1994_2023:
    :cvar VALUE_2013_2007_1991_2011_2027_1971_1974_2029:
    :cvar VALUE_2006_1970_1996_1993_2021:
    :cvar VALUE_1991_2018_1974_1989_2011_1987_1989_1998_1992:
    """
    VALUE_2007_2010_2018_1982_1984_2024 = "2007 2010 2018 1982 1984 2024"
    VALUE_2026_1979_2011_2014_1994_2023 = "2026 1979 2011 2014 1994 2023"
    VALUE_2013_2007_1991_2011_2027_1971_1974_2029 = "2013 2007 1991 2011 2027 1971 1974 2029"
    VALUE_2006_1970_1996_1993_2021 = "2006 1970 1996 1993 2021"
    VALUE_1991_2018_1974_1989_2011_1987_1989_1998_1992 = "1991 2018 1974 1989 2011 1987 1989 1998 1992"


@dataclass
class NistschemaSvIvListGYearEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-gYear-enumeration-5-NS"

    value: Optional[NistschemaSvIvListGYearEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
