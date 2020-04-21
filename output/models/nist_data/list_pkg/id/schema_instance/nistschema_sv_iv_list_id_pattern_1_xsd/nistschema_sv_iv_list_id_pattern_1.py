from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-pattern-1-NS"


@dataclass
class NistschemaSvIvListIdPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-pattern-1"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[\i-[:]][\c-[:]]{2} [\i-[:]][\c-[:]]{57} [\i-[:]][\c-[:]]{31} [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{47} [\i-[:]][\c-[:]]{21}"
        )
    )


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-pattern-1-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
