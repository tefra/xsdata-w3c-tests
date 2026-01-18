from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    value: QName = field(
        metadata={
            "required": True,
            "max_length": 5,
        }
    )
