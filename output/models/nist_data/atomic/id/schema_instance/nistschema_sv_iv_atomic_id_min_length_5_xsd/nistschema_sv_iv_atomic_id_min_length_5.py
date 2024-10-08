from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-minLength-5-NS"


@dataclass
class NistschemaSvIvAtomicIdMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 64,
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-5-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
