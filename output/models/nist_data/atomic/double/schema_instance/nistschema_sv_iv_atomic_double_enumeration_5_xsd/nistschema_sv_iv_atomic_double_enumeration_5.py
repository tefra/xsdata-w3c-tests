from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-5-NS"


class NistschemaSvIvAtomicDoubleEnumeration5Type(Enum):
    """
    :cvar VALUE_1_7976931348623157_E308:
    :cvar VALUE_2_0102746771275176_E_9:
    :cvar VALUE_2_7409799988042133_E_219:
    :cvar VALUE_2_8428374096671001_E96:
    :cvar VALUE_3_6407481234147934_E_114:
    :cvar VALUE_4_6999860123584760_E201:
    :cvar VALUE_4_9_E_324:
    """
    VALUE_1_7976931348623157_E308 = "1.7976931348623157E308"
    VALUE_2_0102746771275176_E_9 = "2.0102746771275176E-9"
    VALUE_2_7409799988042133_E_219 = "2.7409799988042133E-219"
    VALUE_2_8428374096671001_E96 = "2.8428374096671001E96"
    VALUE_3_6407481234147934_E_114 = "3.6407481234147934E-114"
    VALUE_4_6999860123584760_E201 = "4.6999860123584760E201"
    VALUE_4_9_E_324 = "4.9E-324"


@dataclass
class NistschemaSvIvAtomicDoubleEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-double-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicDoubleEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )