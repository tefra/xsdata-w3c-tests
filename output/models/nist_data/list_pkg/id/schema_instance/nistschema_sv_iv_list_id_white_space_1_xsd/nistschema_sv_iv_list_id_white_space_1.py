from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListIdWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-ID-whiteSpace-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-whiteSpace-1-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
