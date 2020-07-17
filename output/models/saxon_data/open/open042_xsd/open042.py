from dataclasses import dataclass, field
from typing import List, Optional
from output.models.saxon_data.open.open042_xsd.open042x import (
    Alpha,
)


@dataclass
class Beta:
    """
    :ivar other_element:
    """
    class Meta:
        name = "beta"

    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar a:
    :ivar b:
    :ivar open_com_element:
    """
    class Meta:
        name = "doc"

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
    open_com_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://open.com/",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
