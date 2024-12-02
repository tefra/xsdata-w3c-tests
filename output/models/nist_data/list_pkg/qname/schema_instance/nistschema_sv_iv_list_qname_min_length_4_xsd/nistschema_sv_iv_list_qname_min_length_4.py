from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-minLength-4-NS"


@dataclass
class NistschemaSvIvListQnameMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-minLength-4"
        namespace = "NISTSchema-SV-IV-list-QName-minLength-4-NS"

    value: list[QName] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        },
    )
