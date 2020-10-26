from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Foo:
    """
    :ivar c:
    :ivar w3_org_1999_xhtml_element_or_d_or_a:
    :ivar b:
    :ivar b2:
    """
    class Meta:
        name = "foo"

    c: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    w3_org_1999_xhtml_element_or_d_or_a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "w3_org/1999/xhtml_element",
                    "tag": "Wildcard",
                    "type": object,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
                {
                    "name": "d",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "a",
                    "type": int,
                    "namespace": "",
                },
            ),
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
