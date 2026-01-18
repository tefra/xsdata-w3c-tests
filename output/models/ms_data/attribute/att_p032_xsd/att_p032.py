from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    att: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
    red_att: str = field(
        init=False,
        default="37",
        metadata={
            "name": "redAtt",
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
    inc_att: str = field(
        init=False,
        default="37",
        metadata={
            "name": "incAtt",
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
    imp_att: str = field(
        init=False,
        default="37",
        metadata={
            "name": "impAtt",
            "type": "Attribute",
            "namespace": "http://importedXSD",
        },
    )


@dataclass(kw_only=True)
class Red:
    class Meta:
        name = "red"

    red_ctatt: None | object = field(
        default=None,
        metadata={
            "name": "redCTAtt",
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
    xx: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | AttRef = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
