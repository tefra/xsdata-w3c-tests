from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class Foo:
    """
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "foo"

    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    bar: Optional["Foo.Bar"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )

    @dataclass
    class Bar:
        """
        :ivar foo:
        :ivar bar:
        """
        foo: Optional[object] = field(
            default=None,
            metadata=dict(
                type="Element",
                namespace="",
                required=True
            )
        )
        bar: Optional["Foo.Bar"] = field(
            default=None,
            metadata=dict(
                type="Element",
                namespace=""
            )
        )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
        namespace = "foo"
