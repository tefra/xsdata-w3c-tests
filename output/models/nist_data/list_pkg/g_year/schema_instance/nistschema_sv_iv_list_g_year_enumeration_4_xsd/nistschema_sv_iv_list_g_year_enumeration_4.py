from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-enumeration-4-NS"


class NistschemaSvIvListGYearEnumeration4Type(Enum):
    """
    :cvar VALUE_2029_2017_2010_1977_1990_2018_1972:
    :cvar VALUE_2015_2029_1998_1997_2022_2001_2001_1985:
    :cvar VALUE_1994_1998_2004_2003_2013_2029_2021_1986_1977:
    :cvar VALUE_2029_1987_2012_2006_2007_2024_2010_1970:
    :cvar VALUE_2020_1984_1986_2001_1977_1983_2028_2005_1999_1970:
    """
    VALUE_2029_2017_2010_1977_1990_2018_1972 = "2029 2017 2010 1977 1990 2018 1972"
    VALUE_2015_2029_1998_1997_2022_2001_2001_1985 = "2015 2029 1998 1997 2022 2001 2001 1985"
    VALUE_1994_1998_2004_2003_2013_2029_2021_1986_1977 = "1994 1998 2004 2003 2013 2029 2021 1986 1977"
    VALUE_2029_1987_2012_2006_2007_2024_2010_1970 = "2029 1987 2012 2006 2007 2024 2010 1970"
    VALUE_2020_1984_1986_2001_1977_1983_2028_2005_1999_1970 = "2020 1984 1986 2001 1977 1983 2028 2005 1999 1970"


@dataclass
class NistschemaSvIvListGYearEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gYear-enumeration-4-NS"

    value: Optional[NistschemaSvIvListGYearEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
