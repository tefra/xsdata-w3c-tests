from dataclasses import dataclass, field


@dataclass
class Ids:
    class Meta:
        name = "ids"

    id_attr: str = field(
        default="zxc",
        metadata={
            "type": "Attribute",
        },
    )
    idref_attr: str = field(
        default="zxc",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root(Ids):
    class Meta:
        name = "root"
