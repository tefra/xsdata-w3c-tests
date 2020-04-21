from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicQnamePattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{27}"
        )
    )
