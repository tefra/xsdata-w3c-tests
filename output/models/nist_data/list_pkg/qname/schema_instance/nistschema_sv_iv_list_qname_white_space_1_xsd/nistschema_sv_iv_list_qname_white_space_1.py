from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListQnameWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-QName-whiteSpace-1-NS"

    value: list[QName] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
