from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-minLength-2-NS"


@dataclass
class NistschemaSvIvListIdMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-minLength-2"
        namespace = "NISTSchema-SV-IV-list-ID-minLength-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "min_length": 6,
            "tokens": True,
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-minLength-2-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
