from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class NewDataSet:
    """
    :ivar t1:
    :ivar t2:
    """
    t1: List["NewDataSet.T1"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    t2: List["NewDataSet.T2"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class T1:
        """
        :ivar id:
        """
        id: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Id",
                type="Element",
                namespace="",
                max_length=5
            )
        )

    @dataclass
    class T2:
        """
        :ivar id:
        """
        id: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Id",
                type="Element",
                namespace="",
                max_length=5
            )
        )
