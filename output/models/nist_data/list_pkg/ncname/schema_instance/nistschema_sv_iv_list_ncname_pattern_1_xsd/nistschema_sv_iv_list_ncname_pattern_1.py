from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NCName-pattern-1-NS"


@dataclass
class NistschemaSvIvListNcnamePattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NCName-pattern-1"
        namespace = "NISTSchema-SV-IV-list-NCName-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[\i-[:]][\c-[:]]{39} [\i-[:]][\c-[:]]{15} [\i-[:]][\c-[:]]{23} [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{55} [\i-[:]][\c-[:]]{18} [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{1}"
        )
    )