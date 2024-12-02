from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-maxLength-2-NS"


@dataclass
class NistschemaSvIvListQnameMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-QName-maxLength-2-NS"

    value: list[QName] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
        },
    )
