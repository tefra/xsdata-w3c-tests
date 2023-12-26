from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicIdMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-ID-maxLength-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 58,
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-maxLength-3-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
