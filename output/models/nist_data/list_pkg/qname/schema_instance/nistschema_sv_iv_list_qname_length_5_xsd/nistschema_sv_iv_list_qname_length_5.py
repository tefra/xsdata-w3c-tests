from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-length-5-NS"


@dataclass
class NistschemaSvIvListQnameLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-length-5"
        namespace = "NISTSchema-SV-IV-list-QName-length-5-NS"

    value: List[QName] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 10,
            "tokens": True,
        }
    )
