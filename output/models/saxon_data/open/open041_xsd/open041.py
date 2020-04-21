from dataclasses import dataclass, field
from typing import Optional
from output.models.saxon_data.open.open041_xsd.open041x import (
    Beta,
)


@dataclass
class Alpha:
    class Meta:
        name = "alpha"



@dataclass
class Doc:
    """
    :ivar content:
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "doc"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    a: Optional[Alpha] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[Beta] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
