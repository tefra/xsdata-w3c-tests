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
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[\i-[:]][\c-[:]]{37} [\i-[:]][\c-[:]]{30} [\i-[:]][\c-[:]]{25} [\i-[:]][\c-[:]]{3} [\i-[:]][\c-[:]]{14}"
        )
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
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )