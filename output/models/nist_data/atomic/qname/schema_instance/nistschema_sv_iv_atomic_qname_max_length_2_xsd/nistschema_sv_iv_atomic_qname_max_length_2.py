from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-maxLength-2-NS"


@dataclass
class NistschemaSvIvAtomicQnameMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-maxLength-2"
        namespace = "NISTSchema-SV-IV-atomic-QName-maxLength-2-NS"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "max_length": 4,
        }
    )
