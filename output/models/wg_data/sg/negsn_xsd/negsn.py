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
class N:
    class Meta:
        name = "n"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(default="")


@dataclass(kw_only=True)
class N1:
    class Meta:
        name = "n1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(default="")


@dataclass(kw_only=True)
class S:
    class Meta:
        name = "s"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(default="")


@dataclass(kw_only=True)
class S1:
    class Meta:
        name = "s1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(default="")


@dataclass(kw_only=True)
class T:
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    s1_or_s: None | S1 | S = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "s1",
                    "type": S1,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
            ),
        },
    )
    n: N = field(
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
