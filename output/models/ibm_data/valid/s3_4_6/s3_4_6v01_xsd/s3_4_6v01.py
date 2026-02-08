from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_6"


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"

    a: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 3,
        },
    )


@dataclass(kw_only=True)
class Root(C):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_6"
