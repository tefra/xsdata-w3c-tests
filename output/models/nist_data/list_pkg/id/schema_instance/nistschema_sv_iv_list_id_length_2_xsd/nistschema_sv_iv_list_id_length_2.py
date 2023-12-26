from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-length-2-NS"


@dataclass
class NistschemaSvIvListIdLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-length-2"
        namespace = "NISTSchema-SV-IV-list-ID-length-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-length-2-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
