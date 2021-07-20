from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-minLength-3-NS"


@dataclass
class NistschemaSvIvAtomicIdMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 58,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-minLength-3-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
