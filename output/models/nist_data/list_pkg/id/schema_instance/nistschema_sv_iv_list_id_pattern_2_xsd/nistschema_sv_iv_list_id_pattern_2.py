from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-pattern-2-NS"


@dataclass
class NistschemaSvIvListIdPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-pattern-2"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{36} [\i-[:]][\c-[:]]{42} [\i-[:]][\c-[:]]{37} [\i-[:]][\c-[:]]{23} [\i-[:]][\c-[:]]{20} [\i-[:]][\c-[:]]{4} [\i-[:]][\c-[:]]{36}"
        )
    )


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-2-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )