from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.w3.org/XML/2008/xsdl-exx/ns1"


@dataclass
class T:
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "s1",
                    "type": str,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "name": "s",
                    "type": str,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "name": "n1",
                    "type": str,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "name": "n",
                    "type": str,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##any",
                },
                {
                    "name": "a",
                    "type": str,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "name": "b",
                    "type": str,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "name": "c",
                    "type": str,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
            ),
            "max_occurs": 12,
        }
    )


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class E:
    class Meta:
        name = "e"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class N:
    class Meta:
        name = "n"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class N1:
    class Meta:
        name = "n1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class S:
    class Meta:
        name = "s"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class S1:
    class Meta:
        name = "s1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
