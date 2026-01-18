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
            "required": True,
        }
    )
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_6"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class D(C):
    class Meta:
        name = "d"
