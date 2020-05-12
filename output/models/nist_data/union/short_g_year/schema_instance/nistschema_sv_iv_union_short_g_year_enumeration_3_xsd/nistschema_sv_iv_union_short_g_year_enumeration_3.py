from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-3-NS"


class NistschemaSvIvUnionShortGYearEnumeration3Type(Enum):
    """
    :cvar VALUE_1978:
    :cvar VALUE_1988:
    :cvar VALUE_MINUS_13234:
    :cvar VALUE_MINUS_1:
    :cvar VALUE_509:
    :cvar VALUE_36:
    :cvar VALUE_MINUS_167:
    :cvar VALUE_1974:
    :cvar VALUE_MINUS_17213:
    """
    VALUE_1978 = "1978"
    VALUE_1988 = "1988"
    VALUE_MINUS_13234 = "-13234"
    VALUE_MINUS_1 = "-1"
    VALUE_509 = "509"
    VALUE_36 = "36"
    VALUE_MINUS_167 = "-167"
    VALUE_1974 = "1974"
    VALUE_MINUS_17213 = "-17213"


@dataclass
class NistschemaSvIvUnionShortGYearEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-3"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-3-NS"

    value: Optional[NistschemaSvIvUnionShortGYearEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
