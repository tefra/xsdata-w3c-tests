from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-pattern-4-NS"


@dataclass
class NistschemaSvIvListIdPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-pattern-4"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"[\i-[:]][\c-[:]]{37} [\i-[:]][\c-[:]]{30} [\i-[:]][\c-[:]]{25} [\i-[:]][\c-[:]]{3} [\i-[:]][\c-[:]]{14}",
            "tokens": True,
        }
    )


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-4-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
