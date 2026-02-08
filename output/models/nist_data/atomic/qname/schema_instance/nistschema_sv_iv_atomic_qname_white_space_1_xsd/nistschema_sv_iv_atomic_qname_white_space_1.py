from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicQnameWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-QName-whiteSpace-1-NS"

    value: QName = field(
        metadata={
            "white_space": "collapse",
        }
    )
