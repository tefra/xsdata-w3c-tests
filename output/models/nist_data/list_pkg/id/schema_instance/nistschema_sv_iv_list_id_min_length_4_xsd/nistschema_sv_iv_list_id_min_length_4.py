from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-minLength-4-NS"


@dataclass
class NistschemaSvIvListIdMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-minLength-4"
        namespace = "NISTSchema-SV-IV-list-ID-minLength-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-minLength-4-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
