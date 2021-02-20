from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-pattern-3-NS"


@dataclass
class NistschemaSvIvListQnamePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-pattern-3"
        namespace = "NISTSchema-SV-IV-list-QName-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{55} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{21} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{18} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{41} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{18}",
            "tokens": True,
        }
    )
