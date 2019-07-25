from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.open_group_editor()
            self.group_cache = []
            tree = self.group_editor.window(auto_id="uxAddressTreeView")
            root = tree.tree_root()
            for node in root.children():
                text = node.text()
                self.group_cache.append(Group(name=text))
        return self.group_cache

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()
        self.group_cache = None

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait('visible')

    def close_group_editor(self):
        self.group_editor.close()

    def delete_group_by_index(self, index):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        root.children()[index].select()
        pass