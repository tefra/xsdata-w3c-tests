from dataclasses import dataclass, field
from lxml.etree import QName
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-pattern-1-NS"


@dataclass
class NistschemaSvIvListQnamePattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-pattern-1"
        namespace = "NISTSchema-SV-IV-list-QName-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{45} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{60} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{30} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{46} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{37} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{55} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{54}"
        )
    )