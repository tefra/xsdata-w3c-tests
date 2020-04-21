from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-4-NS"


class NistschemaSvIvUnionShortGYearEnumeration4Type(Enum):
    """
    :cvar VALUE_MINUS_1:
    :cvar VALUE_MINUS_17213:
    :cvar VALUE_MINUS_2:
    :cvar VALUE_MINUS_543:
    :cvar VALUE_MINUS_760:
    :cvar VALUE_1974:
    :cvar VALUE_1983:
    :cvar VALUE_1987:
    :cvar VALUE_442:
    """
    VALUE_MINUS_1 = "-1"
    VALUE_MINUS_17213 = "-17213"
    VALUE_MINUS_2 = "-2"
    VALUE_MINUS_543 = "-543"
    VALUE_MINUS_760 = "-760"
    VALUE_1974 = "1974"
    VALUE_1983 = "1983"
    VALUE_1987 = "1987"
    VALUE_442 = "442"


@dataclass
class NistschemaSvIvUnionShortGYearEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-4"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-4-NS"

    value: Optional[NistschemaSvIvUnionShortGYearEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
