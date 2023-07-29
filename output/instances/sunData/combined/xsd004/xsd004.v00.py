from output.models.sun_data.combined.xsd004.xsd004_xsd.xsd004 import Root
from output.models.sun_data.combined.xsd004.xsd004_xsd.xsd004a_xsdmod import C
from output.models.sun_data.combined.xsd004.xsd004_xsd.xsd004b_xsdmod import B
from output.models.sun_data.combined.xsd004.xsd004_xsd.xsd004b_xsdmod import C
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    choice=[
        Root.SkipAny(
            any_element=[
                AnyElement(
                    qname="{foo}root",
                    text="",
                    children=[
                        AnyElement(
                            qname="{foo}child",
                            text=""
                        ),
                        AnyElement(
                            qname="{bar}nocheck",
                            text="",
                            tail="&#10;&#9;&#9;&#9;mixed is also allowed?&#10;&#9;&#9;",
                            children=[
                                AnyElement(
                                    qname="{zot}nocheck",
                                    text=""
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
        Root.LaxAny(
            any_element=[
                AnyElement(
                    qname="{foo}undeclared",
                    text="",
                    children=[
                        AnyElement(
                            qname="{bar}a",
                            text=""
                        ),
                        AnyElement(
                            qname="undefined",
                            text=""
                        ),
                    ]
                ),
            ]
        ),
        Root.StrictAny(
            any_element=[
                C(

                ),
                B(

                ),
                C(

                ),
            ]
        ),
        Root.SkipOther(
            other_element=[
                AnyElement(
                    qname="{bob}undeclared",
                    text=""
                ),
                AnyElement(
                    qname="{nowhere}anyThing",
                    text=""
                ),
                AnyElement(
                    qname="{other1}asLongAsInOtherNS",
                    text=""
                ),
                AnyElement(
                    qname="{zot}a",
                    text="",
                    children=[
                        AnyElement(
                            qname="{zot}a",
                            text=""
                        ),
                    ]
                ),
            ]
        ),
        Root.LaxLocal(
            local_element=[
                AnyElement(
                    qname="undeclaredOnly",
                    text=""
                ),
                AnyElement(
                    qname="butLaxlyValidated",
                    text=""
                ),
            ]
        ),
        Root.StrictTarget(
            target_namespace_element=[
                Root(

                ),
                Root(

                ),
                Root(

                ),
            ]
        ),
        Root.SkipBar(
            bar_element=[
                AnyElement(
                    qname="{bar}everything",
                    text=""
                ),
                AnyElement(
                    qname="{bar}in",
                    text=""
                ),
                AnyElement(
                    qname="{bar}bar",
                    text=""
                ),
                AnyElement(
                    qname="{bar}a",
                    text="",
                    children=[
                        AnyElement(
                            qname="{bar}ignore",
                            text=""
                        ),
                    ]
                ),
            ]
        ),
    ]
)
