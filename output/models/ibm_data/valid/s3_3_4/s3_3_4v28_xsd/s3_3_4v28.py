from dataclasses import dataclass, field


@dataclass
class Ids:
    """
    :ivar id_attr:
    :ivar idref_attr:
    """
    class Meta:
        name = "ids"

    id_attr: str = field(
        default="zxc",
        metadata={
            "type": "Attribute",
        }
    )
    idref_attr: str = field(
        default="abc",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root(Ids):
    class Meta:
        name = "root"
