from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-length-4-NS"


@dataclass
class NistschemaSvIvListQnameLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-length-4"
        namespace = "NISTSchema-SV-IV-list-QName-length-4-NS"

    value: List[QName] = field(
        default_factory=list,
        metadata={
            "length": 8,
            "tokens": True,
        },
    )
