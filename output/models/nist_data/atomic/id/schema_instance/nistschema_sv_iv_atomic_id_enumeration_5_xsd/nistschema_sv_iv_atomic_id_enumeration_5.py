from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-5-NS"


class NistschemaSvIvAtomicIdEnumeration5Type(Enum):
    BA = "ba"
    CA = "ca"
    EFOR = "efor"
    HREGISTRY_AS_ON_WORK_U = "hregistry.as.on-work.u"
    ITS_INCLUD = "_its-includ"


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-5-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIdEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-5-NS"

    value: NistschemaSvIvAtomicIdEnumeration5Type = field()
