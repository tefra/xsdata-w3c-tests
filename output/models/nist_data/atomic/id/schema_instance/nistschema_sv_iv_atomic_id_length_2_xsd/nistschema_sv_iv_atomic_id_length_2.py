from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-length-2-NS"


@dataclass
class NistschemaSvIvAtomicIdLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-length-2"
        namespace = "NISTSchema-SV-IV-atomic-ID-length-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 57,
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-length-2-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
