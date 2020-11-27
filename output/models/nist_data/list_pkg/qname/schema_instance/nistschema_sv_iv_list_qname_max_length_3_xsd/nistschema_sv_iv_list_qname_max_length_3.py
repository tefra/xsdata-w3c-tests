from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-maxLength-3-NS"


@dataclass
class NistschemaSvIvListQnameMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-QName-maxLength-3-NS"

    value: List[QName] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 7,
            "tokens": True,
        }
    )
