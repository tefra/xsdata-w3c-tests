from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-maxLength-2-NS"


@dataclass
class NistschemaSvIvAtomicIdMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-maxLength-2"
        namespace = "NISTSchema-SV-IV-atomic-ID-maxLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 62,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-maxLength-2-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
