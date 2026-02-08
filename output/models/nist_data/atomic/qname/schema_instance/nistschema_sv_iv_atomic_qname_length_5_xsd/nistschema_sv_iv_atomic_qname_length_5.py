from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-length-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-length-5"
        namespace = "NISTSchema-SV-IV-atomic-QName-length-5-NS"

    value: QName = field(
        metadata={
            "length": 64,
        }
    )
