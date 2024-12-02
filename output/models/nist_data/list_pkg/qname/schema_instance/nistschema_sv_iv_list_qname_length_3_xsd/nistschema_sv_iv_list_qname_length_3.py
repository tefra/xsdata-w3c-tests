from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-length-3-NS"


@dataclass
class NistschemaSvIvListQnameLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-length-3"
        namespace = "NISTSchema-SV-IV-list-QName-length-3-NS"

    value: list[QName] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
