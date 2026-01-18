from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-length-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListQnameLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-length-1"
        namespace = "NISTSchema-SV-IV-list-QName-length-1-NS"

    value: list[QName] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )
