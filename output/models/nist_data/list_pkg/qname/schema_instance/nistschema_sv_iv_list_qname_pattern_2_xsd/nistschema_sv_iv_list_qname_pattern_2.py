from dataclasses import dataclass, field
from lxml.etree import QName
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-pattern-2-NS"


@dataclass
class NistschemaSvIvListQnamePattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-pattern-2"
        namespace = "NISTSchema-SV-IV-list-QName-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{47} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{11} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{35} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{11} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{43} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{32} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{22} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{21} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{46} ([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{33}"
        )
    )