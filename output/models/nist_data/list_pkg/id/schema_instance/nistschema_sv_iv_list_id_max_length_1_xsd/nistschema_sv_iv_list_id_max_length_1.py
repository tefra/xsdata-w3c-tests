from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-maxLength-1-NS"


@dataclass
class NistschemaSvIvListIdMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-ID-maxLength-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-maxLength-1-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
