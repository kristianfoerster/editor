from dataclasses import dataclass
from pathlib import Path

class JumpListItemLink:
    def __init__(self, *args, **kwargs):
        pass

class JumpListItems:
    def __init__(self):
        self._items = []
    @property
    def items(self):
        return None
    def add(self, item):
        pass

class JumpList:
    def __init__(self):
        self.tasks = JumpListItems()
        self.recent_files = JumpListItems()
    def add_task(self, *args, **kwargs):
        pass
    def add_recent_file(self, *args, **kwargs):
        pass
    def update(self):
        pass
    def erase(self):
        pass