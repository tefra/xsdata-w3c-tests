from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-length-1-NS"


@dataclass
class NistschemaSvIvListIdLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-length-1"
        namespace = "NISTSchema-SV-IV-list-ID-length-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-length-1-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
