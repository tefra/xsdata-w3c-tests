from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/XML/2008/xsdl-exx/ns1"


@dataclass
class T:
    e_or_e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e",
                    "type": str,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
                {
                    "name": "e1",
                    "type": int,
                    "namespace": "http://www.w3.org/XML/2008/xsdl-exx/ns1",
                },
            ),
        }
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
        }
    )


@dataclass
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
