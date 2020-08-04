from dataclasses import dataclass, field
from lxml.etree import QName
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-maxLength-1-NS"


@dataclass
class NistschemaSvIvListQnameMaxLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-QName-maxLength-1-NS"

    value: List[QName] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            max_length=5,
            tokens=True
        )
    )
