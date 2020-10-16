from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-5-NS"


class NistschemaSvIvAtomicPositiveIntegerEnumeration5Type(Enum):
    """
    :cvar VALUE_85265:
    :cvar VALUE_2633:
    :cvar VALUE_20007586335496:
    :cvar VALUE_24394:
    :cvar VALUE_15836086414917927:
    :cvar VALUE_84017762294:
    :cvar VALUE_378362663062:
    """
    VALUE_85265 = 85265
    VALUE_2633 = 2633
    VALUE_20007586335496 = 20007586335496
    VALUE_24394 = 24394
    VALUE_15836086414917927 = 15836086414917927
    VALUE_84017762294 = 84017762294
    VALUE_378362663062 = 378362663062


@dataclass
class NistschemaSvIvAtomicPositiveIntegerEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicPositiveIntegerEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
