from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    att: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    red_att: str = field(
        init=False,
        default="37",
        metadata={
            "name": "redAtt",
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    inc_att: str = field(
        init=False,
        default="37",
        metadata={
            "name": "incAtt",
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    imp_att: str = field(
        init=False,
        default="37",
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

    red_ctatt: Optional[object] = field(
        default=None,
        metadata={
            "name": "redCTAtt",
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
    xx: Optional[object] = field(
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
            "required": True,
        }
    )
