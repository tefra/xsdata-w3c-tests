from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-length-1-NS"


@dataclass
class NistschemaSvIvAtomicIdLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-length-1"
        namespace = "NISTSchema-SV-IV-atomic-ID-length-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 1,
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-length-1-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
