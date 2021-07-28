from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-5-NS"


class NistschemaSvIvAtomicIdEnumeration5Type(Enum):
    BA = "ba"
    CA = "ca"
    EFOR = "efor"
    HREGISTRY_AS_ON_WORK_U = "hregistry.as.on-work.u"
    ITS_INCLUD = "_its-includ"


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-5-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class NistschemaSvIvAtomicIdEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicIdEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
