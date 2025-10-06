
class Seq:


    def __init__(self, header: str, sequence: str):

        self.header = header.strip()
        self.sequence = sequence.upper().replace(" ", "").replace("\n", "")

    def __str__(self) -> str:

        return f">{self.header}\n{self.sequence}"

    def __len__(self) -> int:

        return len(self.sequence)

    def get_alphabet(self) -> str:

        if not self.sequence:
            return "unknown"
        protein_only_chars = set("DEFHIJKLMNPQRSUVWY")
        nucleotide_only_chars = set("U")
        common_chars = set("ACGT")

        unique_chars = set(self.sequence)


        protein_count = len([char for char in unique_chars if char in protein_only_chars])
        nucleotide_count = len([char for char in unique_chars if char in nucleotide_only_chars])


        if protein_count > 0:
            return "protein"
        elif nucleotide_count > 0:
            return "nucleotide"
        elif unique_chars.issubset(common_chars):
            return "nucleotide"
        else:
            return "unknown"
