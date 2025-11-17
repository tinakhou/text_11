import sys
import argparse

# Глобальные константы
CODON_TABLE = {
    "AUG": "M", # старт
    "GCC": "A", "GCG": "A", "GCA": "A", "GCU": "A",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R", "AGA": "R", "AGG": "R",
    "UAA": "*", "UAG": "*", "UGA": "*",
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "UAU": "Y", "UAC": "Y",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C",
    "UGG": "W",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

STOP_CODONS = {"UAA", "UAG", "UGA"}

def main():
    parser = argparse.ArgumentParser(description='Translate RNA to protein')
    parser.add_argument('input', help='Input RNA sequence or file')
    parser.add_argument('-o', '--output', help='Output file (optional)')
    parser.add_argument('--start', type=int, default=0, 
                       help='Start position for translation (default: 0)')
    
    args = parser.parse_args()
    
    try:
        # Получаем входные данные
        rna_sequence = get_input(args.input)
        protein = translate_rna(rna_sequence, args.start)
        
        # Выводим результат
        if args.output:
            with open(args.output, 'w') as f:
                f.write(protein)
            print(f"Protein sequence saved to {args.output}")
        else:
            print(protein)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def get_input(input_arg):
    """Получаем последовательность РНК из файла или прямо из аргумента"""
    try:
        with open(input_arg, 'r') as f:
            content = f.read().strip()
            if not content:
                raise ValueError("Input file is empty")
            return content
    except FileNotFoundError:
        return input_arg
    
def translate_rna(rna_sequence, start_pos=0):
    """Основная функция трансляции с обработкой ошибок"""
    
    # Проверка входных данных
    if not rna_sequence:
        raise ValueError("Empty RNA sequence provided")
    
    # Убираем возможные пробелы и переводим в верхний регистр
    rna_sequence = rna_sequence.strip().upper()
    
    # Проверка допустимых символов
    valid_nucleotides = {'A', 'U', 'G', 'C'}
    invalid_chars = set(rna_sequence) - valid_nucleotides
    if invalid_chars:
        raise ValueError(f"Invalid characters in RNA sequence: {invalid_chars}")
    
    # Проверка позиции старта
    if start_pos < 0 or start_pos >= len(rna_sequence):
        raise ValueError(f"Invalid start position: {start_pos}")
    
    # Основная логика трансляции
    protein = ""
    for i in range(start_pos, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        
        # Проверка на неполный кодон в конце
        if len(codon) < 3:
            print(f"Warning: Incomplete codon '{codon}' at the end of sequence", 
                  file=sys.stderr)
            break
            
        if codon in STOP_CODONS:
            break
            
        try:
            amino_acid = CODON_TABLE[codon]
            protein += amino_acid
        except KeyError:
            raise ValueError(f"Unknown codon: {codon}")
    
    if not protein:
        raise ValueError("No protein sequence generated - check input data")
    
    return protein

def test():
    """Функция для тестирования"""
    sample_input = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    result = translate_rna(sample_input)
    expected = "MAMAPRTEINSTRING"
    print(f"Test: {result == expected}")
    print(f"Input: {sample_input}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")

if __name__ == "__main__":
    # Если скрипт запущен напрямую, а не импортирован
    if len(sys.argv) == 1:
        # Если нет аргументов командной строки - запускаем тест
        test()
    else:
        # Если есть аргументы - запускаем основную программу
        main()