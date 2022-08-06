from output.models.sun_data.combined.xsd021.xsd021_xsd.xsd021 import Root


obj = Root(
    choice=[
        Root.SkipAny(
            any_attributes={
                "{foo}a": "bra",
                "{foo}b": "bra",
                "{undeclared}something": "also allowed",
            }
        ),
        Root.SkipAny(
            any_attributes={}
        ),
        Root.LaxAny(
            any_attributes={
                "{foo}a": "5",
                "{foo}undeclared": "OK",
                "{bar}b": "2",
                "{undeclared}something": "also allowed",
            }
        ),
        Root.LaxAny(
            any_attributes={}
        ),
        Root.StrictAny(
            any_attributes={
                "{foo}b": "5",
                "{bar}c": "2",
                "{zot}a": "52",
            }
        ),
        Root.StrictAny(
            any_attributes={}
        ),
        Root.SkipOther(
            other_attributes={
                "{bar}a": "brabra",
                "{bar}undeclared": "OK",
                "{undeclared}something": "OK",
                "{undeclared}local": "OK",
            }
        ),
        Root.SkipOther(
            other_attributes={}
        ),
        Root.LaxLocal(
            local_attributes={
                "att": "whatever",
            }
        ),
        Root.LaxLocal(
            local_attributes={}
        ),
        Root.StrictTarget(
            target_namespace_attributes={
                "{foo}a": "1",
                "{foo}b": "2",
                "{foo}c": "3",
            }
        ),
        Root.StrictTarget(
            target_namespace_attributes={}
        ),
        Root.SkipBar(
            bar_attributes={
                "{bar}b": "invali",
                "{bar}undeclared": "ok",
            }
        ),
        Root.SkipBar(
            bar_attributes={}
        ),
    ]
)
