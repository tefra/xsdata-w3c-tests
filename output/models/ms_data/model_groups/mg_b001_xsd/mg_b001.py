from dataclasses import dataclass


@dataclass
class Bar:
    class Meta:
        name = "bar"



@dataclass
class Root(Bar):
    class Meta:
        name = "root"
