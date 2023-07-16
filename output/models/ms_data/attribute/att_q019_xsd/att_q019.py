from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    aga1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    aga2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    imported_xsd_aga1: Optional[str] = field(
        default=None,
        metadata={
            "name": "aga1",
            "type": "Attribute",
            "namespace": "http://importedXSD",
        }
    )
    imported_xsd_aga2: Optional[str] = field(
        default=None,
        metadata={
            "name": "aga2",
            "type": "Attribute",
            "namespace": "http://importedXSD",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[AttRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
