from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-length-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-length-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-length-4-NS"

    value: QName = field(
        metadata={
            "length": 34,
        }
    )
