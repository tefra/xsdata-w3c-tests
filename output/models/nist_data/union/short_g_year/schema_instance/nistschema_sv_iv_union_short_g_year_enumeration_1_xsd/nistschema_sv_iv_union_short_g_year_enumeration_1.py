from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-1-NS"


class NistschemaSvIvUnionShortGYearEnumeration1Type(Enum):
    """
    :cvar VALUE_1974:
    :cvar VALUE_1990:
    :cvar VALUE_1993:
    :cvar VALUE_1995:
    :cvar VALUE_2010:
    :cvar VALUE_384:
    :cvar VALUE_39:
    :cvar VALUE_MINUS_962:
    """
    VALUE_1974 = "1974"
    VALUE_1990 = "1990"
    VALUE_1993 = "1993"
    VALUE_1995 = "1995"
    VALUE_2010 = "2010"
    VALUE_384 = "384"
    VALUE_39 = "39"
    VALUE_MINUS_962 = "-962"


@dataclass
class NistschemaSvIvUnionShortGYearEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-1"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-1-NS"

    value: Optional[NistschemaSvIvUnionShortGYearEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
