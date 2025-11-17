import sys
import argparse

def find_substring_locations(s, t):
    """
    Находит все начальные позиции подстроки t в строке s
    Позиции считаются с 1
    """
    #проверка входных данных
    if not s or not t:
        raise ValueError("Both strings must be non-empty")
    
    if len(t) > len(s):
        raise ValueError("Substring t cannot be longer than string s")
    
    locations = []
    len_t = len(t)
    
    #проходим возможным начальным позициям
    for i in range(len(s) - len_t + 1):
        #проверяем совпадение подстроки начиная с позиции i
        if s[i:i + len_t] == t:
            locations.append(i + 1)  # +1 потому что позиции с 1
    
    return locations

def main():
    parser = argparse.ArgumentParser(description='Find all locations of substring t in string s')
    parser.add_argument('s', help='Main string')
    parser.add_argument('t', help='Substring to find')
    parser.add_argument('-o', '--output', help='Output file (optional)')
    parser.add_argument('--test', action='store_true', help='Run test cases')
    
    args = parser.parse_args()
    #основн код
    try:
        if args.test:
            run_tests()
            return
            
        #поиск позиций
        locations = find_substring_locations(args.s, args.t)
        
        #форматир
        result = " ".join(map(str, locations))
        
        #вывод
        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"Results saved to {args.output}")
        else:
            print(result)
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

def run_tests():
    """Запуск тестовых случаев"""
    test_cases = [
        ("GATATATGCATATACTT", "ATAT", [2, 4, 10]),
        ("AAAA", "AA", [1, 2, 3]),
        ("ABC", "D", []),
        ("TEST", "TEST", [1]),
    ]
    
    print("Running tests...")
    all_passed = True
    
    for i, (s, t, expected) in enumerate(test_cases, 1):
        try:
            result = find_substring_locations(s, t)
            passed = result == expected
            status = "PASS" if passed else "FAIL"
            print(f"Test {i}: {status} | s='{s}', t='{t}'")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            
            if not passed:
                all_passed = False
                
        except Exception as e:
            print(f"Test {i}: ERROR | {e}")
            all_passed = False
    
    print(f"\nOverall: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")

def get_input_from_file(filename):
    """Чтение входных данных из файла"""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if len(lines) < 2:
                raise ValueError("File must contain at least 2 lines")
            return lines[0].strip(), lines[1].strip()
    except FileNotFoundError:
        raise ValueError(f"File not found: {filename}")

if __name__ == "__main__":
    #если нет аргументов, использовать старый интерфейс
    if len(sys.argv) == 1:
        try:
            s = input("Enter string s: ").strip()
            t = input("Enter substring t: ").strip()
            locations = find_substring_locations(s, t)
            print(" ".join(map(str, locations)))
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
    else:
        main()