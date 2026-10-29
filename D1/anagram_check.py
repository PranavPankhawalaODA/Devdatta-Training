
from collections import Counter

def normalize(text: str) -> list[str]:
   return [c for c in text.lower() if not c.isspace()]

def is_anagram(a: str, b: str) -> bool:
   return Counter(normalize(a)) == Counter(normalize(b))



def main() -> None:
   
   while True:
       first = input("First string (q to quit): ")
       if first.strip().lower() == "q":
           break
       second = input("Second string: ")
       result = "ARE" if is_anagram(first, second) else "are NOT"
       print(f'"{first}" and "{second}" {result} anagrams.\n')

if __name__ == "__main__":
   main()