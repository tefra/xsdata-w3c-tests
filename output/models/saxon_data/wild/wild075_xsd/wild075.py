from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"

    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"

    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    a: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class Root(Zing):
    class Meta:
        name = "root"
