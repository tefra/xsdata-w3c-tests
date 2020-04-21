from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar test:
    """
    class Meta:
        name = "doc"

    test: Optional["Doc.Test"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    @dataclass
    class Test:
        """
        :ivar foo:
        """
        foo: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )
