from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-pattern-5-NS"


@dataclass
class NistschemaSvIvListIdPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-pattern-5"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[\i-[:]][\c-[:]]{59} [\i-[:]][\c-[:]]{51} [\i-[:]][\c-[:]]{49} [\i-[:]][\c-[:]]{43} [\i-[:]][\c-[:]]{28} [\i-[:]][\c-[:]]{11} [\i-[:]][\c-[:]]{28} [\i-[:]][\c-[:]]{15}",
            "tokens": True,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-5-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
