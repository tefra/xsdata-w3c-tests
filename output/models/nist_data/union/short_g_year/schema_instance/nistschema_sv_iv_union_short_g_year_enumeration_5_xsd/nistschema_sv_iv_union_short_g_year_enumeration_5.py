from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-5-NS"


class NistschemaSvIvUnionShortGYearEnumeration5Type(Enum):
    """
    :cvar VALUE_1278:
    :cvar VALUE_1970:
    :cvar VALUE_1987:
    :cvar VALUE_1988:
    :cvar VALUE_1993:
    :cvar VALUE_2010:
    :cvar VALUE_80:
    """
    VALUE_1278 = "1278"
    VALUE_1970 = "1970"
    VALUE_1987 = "1987"
    VALUE_1988 = "1988"
    VALUE_1993 = "1993"
    VALUE_2010 = "2010"
    VALUE_80 = "80"


@dataclass
class NistschemaSvIvUnionShortGYearEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-5"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-5-NS"

    value: Optional[NistschemaSvIvUnionShortGYearEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
