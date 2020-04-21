from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NCName-pattern-5-NS"


@dataclass
class NistschemaSvIvListNcnamePattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NCName-pattern-5"
        namespace = "NISTSchema-SV-IV-list-NCName-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[\i-[:]][\c-[:]]{40} [\i-[:]][\c-[:]]{59} [\i-[:]][\c-[:]]{55} [\i-[:]][\c-[:]]{41} [\i-[:]][\c-[:]]{12} [\i-[:]][\c-[:]]{25}"
        )
    )
