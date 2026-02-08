from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-length-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-length-1"
        namespace = "NISTSchema-SV-IV-atomic-QName-length-1-NS"

    value: QName = field(
        metadata={
            "length": 1,
        }
    )
