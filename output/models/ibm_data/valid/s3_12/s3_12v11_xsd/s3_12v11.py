from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xstest-tns"


@dataclass
class Root:
    """
    :ivar meeting:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    meeting: List["Root.Meeting"] = field(
        default_factory=list,
        metadata=dict(
            name="Meeting",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Meeting:
        """
        :ivar beverage:
        :ivar end_time:
        """
        beverage: Optional[Union[int, str]] = field(
            default=None,
            metadata=dict(
                type="Element",
                namespace="",
                required=True
            )
        )
        end_time: Optional[int] = field(
            default=None,
            metadata=dict(
                name="end-time",
                type="Attribute"
            )
        )
