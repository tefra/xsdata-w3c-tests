from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/XML/2008/xsdl-exx/ns1"


@dataclass
class T:
    e: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
        },
    )
    e1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
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
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
