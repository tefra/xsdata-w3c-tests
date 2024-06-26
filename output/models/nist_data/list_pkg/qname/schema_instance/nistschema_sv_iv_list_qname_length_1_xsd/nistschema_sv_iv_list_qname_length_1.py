from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-length-1-NS"


@dataclass
class NistschemaSvIvListQnameLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-length-1"
        namespace = "NISTSchema-SV-IV-list-QName-length-1-NS"

    value: List[QName] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )
