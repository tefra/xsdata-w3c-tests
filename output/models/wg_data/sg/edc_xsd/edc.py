from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/XML/2008/xsdl-exx/ns1"


@dataclass(kw_only=True)
class E:
    class Meta:
        name = "e"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(default="")


@dataclass(kw_only=True)
class E1:
    class Meta:
        name = "e1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class T:
    e: None | E = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
        },
    )
    e1: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
        }
    )


@dataclass(kw_only=True)
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
