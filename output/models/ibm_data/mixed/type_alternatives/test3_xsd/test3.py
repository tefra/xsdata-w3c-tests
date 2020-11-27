from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class MinimalA:
    class Meta:
        name = "MINIMAL_A"

    b: Optional[int] = field(
        default=None,
        metadata={
            "name": "B",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class X:
    a: Optional[Union[MinimalA, "X.ACastAsXsBoolean"]] = field(
        default=None,
        metadata={
            "name": "A",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    a_attribute: Optional[bool] = field(
        default=None,
        metadata={
            "name": "a",
            "type": "Attribute",
        }
    )

    @dataclass
    class ACastAsXsBoolean(MinimalA):
        pass
