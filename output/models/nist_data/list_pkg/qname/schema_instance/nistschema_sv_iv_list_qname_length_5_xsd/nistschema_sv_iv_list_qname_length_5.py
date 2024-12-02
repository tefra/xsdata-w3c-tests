from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-length-5-NS"


@dataclass
class NistschemaSvIvListQnameLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-length-5"
        namespace = "NISTSchema-SV-IV-list-QName-length-5-NS"

    value: list[QName] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
