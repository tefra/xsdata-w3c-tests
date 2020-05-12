from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-5-NS"


class NistschemaSvIvAtomicIdEnumeration5Type(Enum):
    """
    :cvar BA:
    :cvar CA:
    :cvar EFOR:
    :cvar HREGISTRY_AS_ON_WORK_U:
    :cvar ITS_INCLUD:
    """
    BA = "ba"
    CA = "ca"
    EFOR = "efor"
    HREGISTRY_AS_ON_WORK_U = "hregistry.as.on-work.u"
    ITS_INCLUD = "_its-includ"


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-5-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicIdEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicIdEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
