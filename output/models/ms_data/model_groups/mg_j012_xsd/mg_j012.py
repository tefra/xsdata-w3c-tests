from dataclasses import dataclass


@dataclass
class Foo:
    class Meta:
        name = "foo"


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
