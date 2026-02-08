from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"

    value: XmlDate = field()


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    a: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    local_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class Root(Zing):
    class Meta:
        name = "root"
