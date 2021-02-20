from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-pattern-3-NS"


@dataclass
class NistschemaSvIvListIdPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-pattern-3"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[\i-[:]][\c-[:]]{23} [\i-[:]][\c-[:]]{17} [\i-[:]][\c-[:]]{11} [\i-[:]][\c-[:]]{50} [\i-[:]][\c-[:]]{12} [\i-[:]][\c-[:]]{53} [\i-[:]][\c-[:]]{61} [\i-[:]][\c-[:]]{20} [\i-[:]][\c-[:]]{25}",
            "tokens": True,
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-3-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
