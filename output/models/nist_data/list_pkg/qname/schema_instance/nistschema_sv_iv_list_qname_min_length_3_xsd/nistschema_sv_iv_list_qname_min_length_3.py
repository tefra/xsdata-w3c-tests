from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-minLength-3-NS"


@dataclass
class NistschemaSvIvListQnameMinLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-minLength-3"
        namespace = "NISTSchema-SV-IV-list-QName-minLength-3-NS"

    value: List[QName] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=7,
            tokens=True
        )
    )
