from dataclasses import dataclass, field
from lxml.etree import QName
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-minLength-4-NS"


@dataclass
class NistschemaSvIvListQnameMinLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-minLength-4"
        namespace = "NISTSchema-SV-IV-list-QName-minLength-4-NS"

    value: List[QName] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=8,
            tokens=True
        )
    )
