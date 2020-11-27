from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    att: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    red_att: Optional[str] = field(
        default=None,
        metadata={
            "name": "redAtt",
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    inc_att: Optional[str] = field(
        default=None,
        metadata={
            "name": "incAtt",
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    imp_att: Optional[str] = field(
        default=None,
        metadata={
            "name": "impAtt",
            "type": "Attribute",
            "namespace": "http://importedXSD",
        }
    )


@dataclass
class Red:
    class Meta:
        name = "red"

    red_ctatt: Optional[str] = field(
        default=None,
        metadata={
            "name": "redCTAtt",
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    xx: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
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
        }
    )
