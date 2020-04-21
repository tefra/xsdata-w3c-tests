from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar element1:
    """
    class Meta:
        name = "root"

    element1: Optional["Root.Element1"] = field(
        default=None,
        metadata=dict(
            name="Element1",
            type="Element",
            namespace="",
            required=True
        )
    )

    @dataclass
    class Element1:
        """
        :ivar group2_element1:
        :ivar group2_element2:
        """
        group2_element1: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="Group2_Element1",
                type="Element",
                namespace="",
                min_occurs=2,
                max_occurs=9223372036854775807,
                sequential=True
            )
        )
        group2_element2: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="Group2_Element2",
                type="Element",
                namespace="",
                min_occurs=2,
                max_occurs=9223372036854775807,
                sequential=True
            )
        )
