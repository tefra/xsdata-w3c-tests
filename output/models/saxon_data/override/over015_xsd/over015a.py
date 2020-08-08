from dataclasses import dataclass, field
from typing import Optional
from output.models.saxon_data.override.over015_xsd.over015 import NotaFooBar


@dataclass
class StructuredDate:
    """
    :ivar year:
    :ivar month:
    :ivar day:
    :ivar nota:
    """
    class Meta:
        name = "structuredDate"

    year: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    month: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    day: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    nota: Optional[NotaFooBar] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
