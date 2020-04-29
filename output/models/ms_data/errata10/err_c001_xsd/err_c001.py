from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class Root:
    """
    :ivar test_attr:
    """
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    test_attr: object = field(
        init=False,
        default="This   is   a    fixed value",
        metadata=dict(
            name="testAttr",
            type="Attribute"
        )
    )
