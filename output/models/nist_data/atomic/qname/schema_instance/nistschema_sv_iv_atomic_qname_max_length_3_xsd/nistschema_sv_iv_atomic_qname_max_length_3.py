from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-maxLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-QName-maxLength-3-NS"

    value: QName = field(
        metadata={
            "max_length": 57,
        }
    )
