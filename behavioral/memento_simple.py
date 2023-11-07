import logging

logging.basicConfig(level="INFO")


class Memento:
    """Memento class for saving the data."""

    def __init__(self, file, content):
        """Put all your file content here"""
        self.file = file
        self.content = content


class FileWriterUtility:
    """It's a File Writing Utility"""

    def __init__(self, file):
        """Store the input file data"""
        self.file = file
        self.content = ""

    def write(self, string):
        """Write the data into the file"""
        self.content += string

    def save(self):
        """Save the data into the Memento"""
        return Memento(self.file, self.content)

    def undo(self, memento):
        """UNDO feature provided"""
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    """CareTaker for FileWriter"""

    def save(self, writer):
        """Saves the data"""
        self.obj = writer.save()

    def undo(self, writer):
        """Undo the content"""
        writer.undo(self.obj)


def main():
    # Create the caretaker object
    caretaker = FileWriterCaretaker()

    # Create the writer object
    writer = FileWriterUtility("GFG.txt")

    # Write data into file using writer object
    writer.write("First vision\n")
    logging.info(writer.content + "\n\n")

    # Save the file
    caretaker.save(writer)

    # Again write using the writer
    writer.write("Second vision\n")

    logging.info(writer.content + "\n\n")

    # Undo the file
    caretaker.undo(writer)

    logging.info(writer.content + "\n\n")


if __name__ == "__main__":
    main()
