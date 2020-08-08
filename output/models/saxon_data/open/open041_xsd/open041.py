from dataclasses import dataclass, field
from typing import List, Optional
from output.models.saxon_data.open.open041_xsd.open041x import Beta


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

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
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
