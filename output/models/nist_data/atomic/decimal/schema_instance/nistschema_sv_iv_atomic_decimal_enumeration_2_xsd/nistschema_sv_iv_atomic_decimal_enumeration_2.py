from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-enumeration-2-NS"


class NistschemaSvIvAtomicDecimalEnumeration2Type(Enum):
    """
    :cvar VALUE_61113534938_0:
    :cvar VALUE_0_575:
    :cvar VALUE_108747_8431:
    :cvar VALUE_31588397646362_1:
    :cvar VALUE_7_682949472786:
    :cvar VALUE_729089_6:
    :cvar VALUE_8_843008676:
    :cvar VALUE_89_20902289982400:
    :cvar VALUE_89_98169071278:
    """
    VALUE_61113534938_0 = "-61113534938.0"
    VALUE_0_575 = "0.575"
    VALUE_108747_8431 = "108747.8431"
    VALUE_31588397646362_1 = "31588397646362.1"
    VALUE_7_682949472786 = "7.682949472786"
    VALUE_729089_6 = "729089.6"
    VALUE_8_843008676 = "8.843008676"
    VALUE_89_20902289982400 = "89.20902289982400"
    VALUE_89_98169071278 = "89.98169071278"


@dataclass
class NistschemaSvIvAtomicDecimalEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicDecimalEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
