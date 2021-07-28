from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-length-4-NS"


@dataclass
class NistschemaSvIvAtomicIdLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-length-4"
        namespace = "NISTSchema-SV-IV-atomic-ID-length-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "length": 8,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-length-4-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
