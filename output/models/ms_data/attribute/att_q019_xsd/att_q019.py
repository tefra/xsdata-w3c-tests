from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    aga1: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
    aga2: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
    imported_xsd_aga1: None | str = field(
        default=None,
        metadata={
            "name": "aga1",
            "type": "Attribute",
            "namespace": "http://importedXSD",
        },
    )
    imported_xsd_aga2: None | str = field(
        default=None,
        metadata={
            "name": "aga2",
            "type": "Attribute",
            "namespace": "http://importedXSD",
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
