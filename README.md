Класс Seq
Назначение: Представление биологической последовательности из FASTA формата.

Атрибуты:

header (str): Заголовок последовательности (без символа '>')

sequence (str): Биологическая последовательность без пробелов и переносов строк

Методы:

__init__(header: str, sequence: str): Инициализация последовательности

__str__() -> str: Возвращает строковое представление в формате FASTA

__len__() -> int: Возвращает длину последовательности

get_alphabet() -> str: Определяет тип последовательности ('nucleotide', 'protein', 'unknown')

Класс FastaReader
Назначение: Чтение и парсинг файлов в формате FASTA.

Атрибуты:

filename (str): Путь к FASTA файлу

Методы:

__init__(filename: str): Инициализация ридера

is_valid_fasta() -> bool: Проверяет соответствие файла формату FASTA

read_sequences() -> Generator[Seq, None, None]: Генератор для последовательного чтения последовательностей

Структура
├── fast/
│   ├── __init__.py
│   ├── fasta.py
│   └── seq.py
├── examples/
│   ├── mainseq.py
│   ├── nucleotides.fasta
│   └── proteins.fasta
├── setup.py
└── README.md


