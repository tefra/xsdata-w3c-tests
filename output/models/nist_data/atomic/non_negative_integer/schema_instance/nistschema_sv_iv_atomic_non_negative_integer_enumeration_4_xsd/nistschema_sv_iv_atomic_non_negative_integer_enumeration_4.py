from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-4-NS"


class NistschemaSvIvAtomicNonNegativeIntegerEnumeration4Type(Enum):
    """
    :cvar VALUE_165524680951923075:
    :cvar VALUE_17593746:
    :cvar VALUE_25316000768963:
    :cvar VALUE_5435077718428:
    :cvar VALUE_641253638624229571:
    :cvar VALUE_6809792634202668:
    :cvar VALUE_75086583090071:
    :cvar VALUE_90692:
    """
    VALUE_165524680951923075 = 165524680951923075
    VALUE_17593746 = 17593746
    VALUE_25316000768963 = 25316000768963
    VALUE_5435077718428 = 5435077718428
    VALUE_641253638624229571 = 641253638624229571
    VALUE_6809792634202668 = 6809792634202668
    VALUE_75086583090071 = 75086583090071
    VALUE_90692 = 90692


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicNonNegativeIntegerEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )