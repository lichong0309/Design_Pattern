import os
from abc import ABC, abstractmethod
 
verbose = True
 
class Command(ABC):
 
    @abstractmethod
    def execute(self):
        pass
 
    @abstractmethod
    def undo(self):
        pass
 
class RenameFile(Command):
 
    def __init__(self,src, dest):
        self._src = src
        self._dest = dest
 
    def execute(self):
        if verbose:
            print(f"rename {self._src} with name {self._dest}")
        os.rename(self._src, self._dest)
 
    def undo(self):
        if verbose:
            print(f"rename back from {self._dest} with name {self._src}")
        os.rename(self._dest, self._src)
 
 
class CreateFile(Command):
 
    def __init__(self, file_path, data="Hello python"):
        self._file_path, self._data = file_path, data
 
    def execute(self):
        if verbose:
            print(f"create file:  {self._file_path} with data {self._data}")
        with open(self._file_path, 'w') as f:
            f.write(self._data)
 
    def undo(self):
        if verbose:
            print(f"delete file: {self._file_path}")
        os.remove(self._file_path)
 
class DeleteFile(Command):
    def __init__(self, file_path):
        self._file_path = file_path
        self._tmp_path = self._file_path + ".tmp"
 
    def execute(self):
        if verbose:
            print(f"delete file:  {self._file_path}")
        os.rename(self._file_path, self._tmp_path)
 
    def undo(self):
        if verbose:
            print(f"recover file: {self._file_path}")
        os.rename(self._tmp_path, self._file_path)
 
class Invoker(object):
    command_list = []
    def register_cmd(self, command):
        self.command_list.append(command)
 
    def cancel_cmd(self, command):
        self.command_list.remove(command)
 
    def run_cmd(self):
        for cmd in self.command_list:
            cmd.execute()
 
    def recovery(self):
        for cmd in self.command_list:
            cmd.undo()
 
def main():
    org_file = "test.txt"
    new_file = "demo.txt"
    invoker = Invoker()
    invoker.register_cmd(CreateFile(org_file, u"人生苦短，我用python"))
    invoker.register_cmd(RenameFile(org_file, new_file))
    invoker.register_cmd(DeleteFile(new_file))
 
    invoker.run_cmd()
    invoker.command_list = reversed(invoker.command_list)
    invoker.recovery()
 
 
if __name__ == "__main__":
    main()