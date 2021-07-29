from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicIdWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-ID-whiteSpace-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-whiteSpace-1-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
