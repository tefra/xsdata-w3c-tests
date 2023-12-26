from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicIdPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-ID-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[\i-[:]][\c-[:]]{55}",
        },
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-pattern-2-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
