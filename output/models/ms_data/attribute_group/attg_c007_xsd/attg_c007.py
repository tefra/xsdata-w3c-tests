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
        :ivar att_fix:
        :ivar foo:
        """
        att_fix: int = field(
            init=False,
            default=37,
            metadata=dict(
                name="attFix",
                type="Attribute"
            )
        )
        foo: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )
