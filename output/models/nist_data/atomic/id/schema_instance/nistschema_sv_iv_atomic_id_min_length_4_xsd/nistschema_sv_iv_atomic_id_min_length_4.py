from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-minLength-4-NS"


@dataclass
class NistschemaSvIvAtomicIdMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 6,
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-4-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
