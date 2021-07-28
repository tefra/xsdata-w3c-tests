from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicIdMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 1,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-1-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
