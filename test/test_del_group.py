# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import operator


def test_delete_some_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) == 0:
        app.groups.add_new_group(Group(name="New group"))
    index = randrange(len(old_list))
    app.groups.delete_group_by_index(index)
    new_list = app.groups.get_group_list()
    assert len(old_list) - 1 == len(new_list)
    old_list[index:index+1] = []
    assert sorted(old_list, key=operator.attrgetter('name')) == sorted(new_list, key=operator.attrgetter('name'))
