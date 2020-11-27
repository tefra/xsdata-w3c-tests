from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-enumeration-1-NS"


class NistschemaSvIvListGYearEnumeration1Type(Enum):
    VALUE_2029_1976_2001_1970_2028_1974_2025_2027_1986 = "2029 1976 2001 1970 2028 1974 2025 2027 1986"
    VALUE_1987_1994_1987_2017_2029_1985 = "1987 1994 1987 2017 2029 1985"
    VALUE_2003_2004_2009_1986_1979 = "2003 2004 2009 1986 1979"
    VALUE_2024_2010_2016_2024_2020_2026 = "2024 2010 2016 2024 2020 2026"
    VALUE_2004_2016_2009_1973_2027_1981_1982_2023 = "2004 2016 2009 1973 2027 1981 1982 2023"
    VALUE_2028_2013_1980_2019_2024_2013_2009 = "2028 2013 1980 2019 2024 2013 2009"
    VALUE_2001_1979_1996_2004_2011_2029_2011 = "2001 1979 1996 2004 2011 2029 2011"
    VALUE_2000_2026_1988_2009_1971_2008_2001 = "2000 2026 1988 2009 1971 2008 2001"


@dataclass
class NistschemaSvIvListGYearEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-gYear-enumeration-1-NS"

    value: Optional[NistschemaSvIvListGYearEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
