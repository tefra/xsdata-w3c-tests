from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-length-5-NS"


@dataclass
class NistschemaSvIvListIdLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-length-5"
        namespace = "NISTSchema-SV-IV-list-ID-length-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-length-5-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
