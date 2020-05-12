from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-enumeration-2-NS"


class NistschemaSvIvListGYearEnumeration2Type(Enum):
    """
    :cvar VALUE_2020_2006_1971_1986_1975_1984:
    :cvar VALUE_2029_1983_1986_2015_2017_2004_2010_2021_1978_2008:
    :cvar VALUE_1999_1993_1995_1996_1983_1983_1975_2019_1989:
    :cvar VALUE_1972_1988_2021_2014_2007_2012_2005:
    :cvar VALUE_1970_2023_1975_2019_2024_2019_2021_2001:
    :cvar VALUE_1994_2005_1998_2005_2029_1970_2017:
    :cvar VALUE_1989_2009_1989_2014_1989_1991_1985_1984:
    """
    VALUE_2020_2006_1971_1986_1975_1984 = "2020 2006 1971 1986 1975 1984"
    VALUE_2029_1983_1986_2015_2017_2004_2010_2021_1978_2008 = "2029 1983 1986 2015 2017 2004 2010 2021 1978 2008"
    VALUE_1999_1993_1995_1996_1983_1983_1975_2019_1989 = "1999 1993 1995 1996 1983 1983 1975 2019 1989"
    VALUE_1972_1988_2021_2014_2007_2012_2005 = "1972 1988 2021 2014 2007 2012 2005"
    VALUE_1970_2023_1975_2019_2024_2019_2021_2001 = "1970 2023 1975 2019 2024 2019 2021 2001"
    VALUE_1994_2005_1998_2005_2029_1970_2017 = "1994 2005 1998 2005 2029 1970 2017"
    VALUE_1989_2009_1989_2014_1989_1991_1985_1984 = "1989 2009 1989 2014 1989 1991 1985 1984"


@dataclass
class NistschemaSvIvListGYearEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-gYear-enumeration-2-NS"

    value: Optional[NistschemaSvIvListGYearEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
