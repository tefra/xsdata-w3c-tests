from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-enumeration-2-NS"


class NistschemaSvIvUnionShortGYearEnumeration2Type(Enum):
    """
    :cvar VALUE_1970:
    :cvar VALUE_MINUS_205:
    :cvar VALUE_MINUS_37:
    :cvar VALUE_MINUS_3830:
    :cvar VALUE_MINUS_4097:
    :cvar VALUE_MINUS_8:
    """
    VALUE_1970 = "1970"
    VALUE_MINUS_205 = "-205"
    VALUE_MINUS_37 = "-37"
    VALUE_MINUS_3830 = "-3830"
    VALUE_MINUS_4097 = "-4097"
    VALUE_MINUS_8 = "-8"


@dataclass
class NistschemaSvIvUnionShortGYearEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-enumeration-2"
        namespace = "NISTSchema-SV-IV-union-short-gYear-enumeration-2-NS"

    value: Optional[NistschemaSvIvUnionShortGYearEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
