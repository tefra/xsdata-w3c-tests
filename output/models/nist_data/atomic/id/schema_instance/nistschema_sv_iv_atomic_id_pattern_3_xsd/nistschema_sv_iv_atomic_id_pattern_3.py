from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicIdPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-ID-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[\i-[:]][\c-[:]]{18}",
        }
    )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-pattern-3-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
