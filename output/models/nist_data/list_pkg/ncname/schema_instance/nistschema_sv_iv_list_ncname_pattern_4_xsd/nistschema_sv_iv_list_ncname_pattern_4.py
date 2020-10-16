from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NCName-pattern-4-NS"


@dataclass
class NistschemaSvIvListNcnamePattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-NCName-pattern-4"
        namespace = "NISTSchema-SV-IV-list-NCName-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"[\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{50} [\i-[:]][\c-[:]]{47} [\i-[:]][\c-[:]]{60} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{0} [\i-[:]][\c-[:]]{17} [\i-[:]][\c-[:]]{45} [\i-[:]][\c-[:]]{50} [\i-[:]][\c-[:]]{36}",
            "tokens": True,
        }
    )
