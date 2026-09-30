class File:
    def __init__(self, name):
        self.name = name
        self.content = ""

    def write(self, text):
        self.content += text

    def read(self):
        return self.content


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.directories = {}
        self.parent = None


class FileSystem:
    def __init__(self):
        self.root = Directory("root")
        self.current = self.root

    # Create directory
    def mkdir(self, name):
        if name in self.current.directories:
            print("Directory already exists")
        else:
            new_dir = Directory(name)
            new_dir.parent = self.current
            self.current.directories[name] = new_dir
            print("Directory created")

    # Create file
    def touch(self, name):
        if name in self.current.files:
            print("File already exists")
        else:
            self.current.files[name] = File(name)
            print("File created")

    # List files and folders
    def ls(self):
        print("Directories:")
        for d in self.current.directories:
            print("  [D]", d)

        print("Files:")
        for f in self.current.files:
            print("  [F]", f)

    # Change directory
    def cd(self, name):
        if name == "..":
            if self.current.parent:
                self.current = self.current.parent
        elif name in self.current.directories:
            self.current = self.current.directories[name]
        else:
            print("Directory not found")

    # Write to file
    def write(self, filename, text):
        if filename in self.current.files:
            self.current.files[filename].write(text)
            print("Content written")
        else:
            print("File not found")

    # Read file
    def read(self, filename):
        if filename in self.current.files:
            print(self.current.files[filename].read())
        else:
            print("File not found")

    # Delete file
    def rm(self, name):
        if name in self.current.files:
            del self.current.files[name]
            print("File deleted")
        elif name in self.current.directories:
            del self.current.directories[name]
            print("Directory deleted")
        else:
            print("Not found")

    # Show directory tree
    def tree(self, directory=None, level=0):
        if directory is None:
            directory = self.current

        print("  " * level + "|-- " + directory.name)

        for d in directory.directories.values():
            self.tree(d, level + 1)

        for f in directory.files.values():
            print("  " * (level + 1) + "|-- " + f.name)


# Command Line Interface
def start():
    fs = FileSystem()

    while True:
        command = input("FS> ").split()

        if not command:
            continue

        cmd = command[0]

        if cmd == "mkdir":
            fs.mkdir(command[1])

        elif cmd == "touch":
            fs.touch(command[1])

        elif cmd == "ls":
            fs.ls()

        elif cmd == "cd":
            fs.cd(command[1])

        elif cmd == "write":
            filename = command[1]
            text = " ".join(command[2:])
            fs.write(filename, text)

        elif cmd == "read":
            fs.read(command[1])

        elif cmd == "rm":
            fs.rm(command[1])

        elif cmd == "tree":
            fs.tree()

        elif cmd == "exit":
            break

        else:
            print("Unknown command")


start()


#================output================
# FS> mkdir docs
# Directory created

# FS> cd docs

# FS> touch file1.txt
# File created

# FS> write file1.txt Hello World

# FS> read file1.txt
# Hello World

# FS> ls
# Directories:
# Files:
# [F] file1.txt