from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://www.w3.org/XML/2008/xsdl-exx/ns1"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class E:
    class Meta:
        name = "e"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class N:
    class Meta:
        name = "n"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class N1:
    class Meta:
        name = "n1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class S:
    class Meta:
        name = "s"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class S1:
    class Meta:
        name = "s1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class T:
    choice: List[Union[S1, S, N1, N, A, B, object]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "s1",
                    "type": S1,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                    "max_occurs": 2,
                },
                {
                    "name": "s",
                    "type": S,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                    "max_occurs": 2,
                },
                {
                    "name": "n1",
                    "type": N1,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                    "max_occurs": 2,
                },
                {
                    "name": "n",
                    "type": N,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                    "max_occurs": 2,
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##any",
                },
            ),
            "max_occurs": 10,
        },
    )
    c: Optional[C] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
            "required": True,
        },
    )


@dataclass
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
