from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Foo:
    """
    :ivar a_or_d_or_w3_org_1999_xhtml_element:
    :ivar b:
    :ivar b2:
    :ivar c:
    """
    class Meta:
        name = "foo"

    a_or_d_or_w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "d",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "w3_org/1999/xhtml_element",
                    "tag": "Wildcard",
                    "type": object,
                    "namespace": "http://www.w3.org/1999/xhtml",
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
    c: Optional[bool] = field(
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
