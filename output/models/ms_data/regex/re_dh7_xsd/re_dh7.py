from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar id:
    :ivar elem:
    """
    class Meta:
        name = "doc"

    id: List["Doc.Id"] = field(
        default_factory=list,
        metadata=dict(
            name="ID",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=2
        )
    )
    elem: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=2,
            pattern=r"\c[\c\d]*"
        )
    )

    @dataclass
    class Id:
        """
        :ivar att:
        """
        att: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )
