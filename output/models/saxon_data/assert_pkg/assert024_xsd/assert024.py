from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName


@dataclass
class Test:
    """
    :ivar rule:
    """
    rule: List["Test.Rule"] = field(
        default_factory=list,
        metadata=dict(
            name="Rule",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Rule:
        """
        :ivar name:
        """
        name: Optional[QName] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                required=True
            )
        )
