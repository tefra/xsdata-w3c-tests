from dataclasses import dataclass, field
from lxml.etree import QName
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-pattern-3-NS"


@dataclass
class NistschemaSvIvListQnamePattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-pattern-3"
        namespace = "NISTSchema-SV-IV-list-QName-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{55} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{21} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{18} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{41} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{18}"
        )
    )