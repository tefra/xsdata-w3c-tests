from output.models.sun_data.combined.xsd022.xsd022_xsd.xsd022 import Root


obj = Root(
    child1_or_child2=[
        Root.Child1(
            value=[
                '123456',
                'abcdef',
                'xxxxxxxx',
            ]
        ),
        Root.Child2(
            value=True
        ),
        Root.Child2(
            value=False
        ),
        Root.Child2(
            value=False
        ),
        Root.Child2(
            value=True
        ),
        Root.Child2(
            value='abcdef'
        ),
        Root.Child2(
            value='xxxxxxxx'
        ),
    ]
)
