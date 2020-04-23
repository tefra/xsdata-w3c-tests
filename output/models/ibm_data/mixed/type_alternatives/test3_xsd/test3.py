from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class MinimalA:
    """
    :ivar b:
    """
    class Meta:
        name = "MINIMAL_A"

    b: Optional[int] = field(
        default=None,
        metadata=dict(
            name="B",
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class X:
    """
    :ivar a:
    :ivar a_attribute:
    """
    a: Optional[Union[MinimalA, "X.ACastAsXsBoolean"]] = field(
        default=None,
        metadata=dict(
            name="A",
            type="Element",
            namespace="",
            required=True
        )
    )
    a_attribute: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="a",
            type="Attribute"
        )
    )

    @dataclass
    class ACastAsXsBoolean(MinimalA):
        pass
