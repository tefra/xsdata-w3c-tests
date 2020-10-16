from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicIdPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-ID-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[\i-[:]][\c-[:]]{36}",
        }
    )


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-pattern-5-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
