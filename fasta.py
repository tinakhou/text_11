from .seq import Seq


class FastaReader:


    def __init__(self, file_path: str):

        self.file_path = file_path

    def is_valid_fasta(self) -> bool:

        try:
            with open(self.file_path, 'r') as file:
                first_line = file.readline().strip()

                return first_line.startswith('>')
        except (ErrorFile, ErrorIO):
            return False
            
    def read_records(self):

        try:
            with open(self.file_path, 'r') as file:
                current_header = ""
                current_sequence = ""

                for line in file:
                    line = line.strip()

                if current_header:
                    yield Seq(current_header, current_sequence)

        except Error1:
            raise ErrorFile(f"{self.file_path} не найден")
        except Error2:
            raise ErroriO(f"oшибка чтения {self.file_path}")
