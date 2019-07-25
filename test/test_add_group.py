import operator


def test_add_group(app, xl_groups):
    group = xl_groups
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    old_list.append(group)
    assert sorted(old_list, key=operator.attrgetter('name')) == sorted(new_list, key=operator.attrgetter('name'))
