from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class AttRef:
    class Meta:
        name = "attRef"

    foo: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
    foo_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "foo",
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
