from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://id050.ly/"


@dataclass
class EmpType:
    """
    :ivar name:
    :ivar nr:
    :ivar manager:
    """
    class Meta:
        name = "empType"

    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://id050.ly/",
            required=True
        )
    )
    nr: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://id050.ly/",
            required=True
        )
    )
    manager: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://id050.ly/"
        )
    )


@dataclass
class Doc:
    """
    :ivar emp:
    """
    class Meta:
        name = "doc"
        namespace = "http://id050.ly/"

    emp: List[EmpType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )