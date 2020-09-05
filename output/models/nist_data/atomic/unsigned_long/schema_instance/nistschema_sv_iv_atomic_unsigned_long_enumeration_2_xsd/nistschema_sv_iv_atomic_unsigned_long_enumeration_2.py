from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-2-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration2Type(Enum):
    """
    :cvar VALUE_840115845:
    :cvar VALUE_2874238170314:
    :cvar VALUE_355386265673274248:
    :cvar VALUE_37531498438491484:
    :cvar VALUE_92597973:
    :cvar VALUE_320:
    :cvar VALUE_9340658324154:
    :cvar VALUE_224645440232296156:
    """
    VALUE_840115845 = 840115845
    VALUE_2874238170314 = 2874238170314
    VALUE_355386265673274248 = 355386265673274248
    VALUE_37531498438491484 = 37531498438491484
    VALUE_92597973 = 92597973
    VALUE_320 = 320
    VALUE_9340658324154 = 9340658324154
    VALUE_224645440232296156 = 224645440232296156


@dataclass
class NistschemaSvIvAtomicUnsignedLongEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedLongEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
