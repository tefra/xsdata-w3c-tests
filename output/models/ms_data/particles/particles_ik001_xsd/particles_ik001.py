from dataclasses import dataclass, field
from typing import Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    c1_or_c2: Optional[Union[str, object]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": str,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "c2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )


@dataclass
class R(B):
    pass


@dataclass
class Elem(R):
    class Meta:
        name = "elem"
        namespace = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
