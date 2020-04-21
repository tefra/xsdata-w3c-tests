from dataclasses import dataclass


@dataclass
class Foo123:
    class Meta:
        name = "foo123"



@dataclass
class Root(Foo123):
    class Meta:
        name = "root"
