from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-maxLength-1-NS"


@dataclass
class NistschemaSvIvListQnameMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-QName-maxLength-1-NS"

    value: list[QName] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        },
    )
