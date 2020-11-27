from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-maxLength-5-NS"


@dataclass
class NistschemaSvIvListIdMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-ID-maxLength-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 10,
            "tokens": True,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-maxLength-5-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
