from seq import Seq
from fasta import FastaReader


def demo_seq():
    print("класс Seq")

    protein_seq = Seq("sp|P12345", "WIMSSCLNCEQWSIML")
    dna_seq = Seq(">chr1:100-200", "GGGCTATCATACTC")


    print("белковая")
    print(protein_seq)
    print(f"длина: {len(protein_seq)}")
    print(f"алфавит: {protein_seq.get_alphabet()}")

    print("ДНК последовательность:")
    print(dna_seq)
    print(f"длина: {len(dna_seq)}")
    print(f"алфавит: {dna_seq.get_alphabet()}")


def demo_fasta_reader():
    print("\n" + "=" * 50)
    print("класс FastaReader")

    reader = FastaReader("testfasta")

    print("\nЗаписи из FASTA файла:")
    for i, record in enumerate(reader.read_records(), 1):
        print(f"\n{i}. {record.header}")
        print(f"   Последовательность: {record.sequence[:30]}...")
        print(f"   Длина: {len(record)}")
        print(f"   Алфавит: {record.get_alphabet()}")


if __name__ == "__main__":
    demo_seq()
    demo_fasta_reader()
