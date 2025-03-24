# E1-Implementation-of-Lexical-Analysis-Automaton-and-Regular-Expression-

## Description

Lexical analysis, within the field of computational methods is fundamental to recognizing and validating strings belonging to specific languages. This project aims to design and implement an automaton capable of correctly identifying strings generated solely by combinations of the digits **0**, **1**, and **2**, under certain specific restrictions: the strings **must not contain** the sequences `'1101'`, `'1122'`, `'1011'`, or `'1012'`. Accurat identification of these restricted patterns is crucial to ensure the integrity of the lexical analysis.

To solve this challenge, two complementary approaches were employed. 

First, a **Deterministic Finite Automaton (DFA)** was used—an ideal mathematical tool for recognizing specific language thanks to its defined and deterministic transition capability. A DFA is composed of five essential elements:

- **Q**: Finite set of states.  
- **Σ**: Finite set of input symbols (alphabet).  
- **δ**: Transition function that clearly specifies the next state given an input and a current state.  
- **q₀**: Initial state from which the analysis begins.  
- **F**: Set of acceptance states, where the string is considered valid.  

This automaton was implemented using **Prolog**, taking advantage of its robustness in logical representation and efficient handling of defined transition rules.

In parallel, language validation was addressed using **regular expressions**, implemented in **Python** with the `re` module. Regular expressions offer a compact and eficient method for describing textual patterns and allow rapid verification of the validity of generated strings. Because there is a direct correspondence between regular expressions and finite automata, both methods are comparable and complementary.

Finally, to ensure the accuracy and robustness of the developed system, **two complete sets of automated tests** were created. These provide empirical evidence on the effectivenes of both implementations, highlighting aspects such as computational efficiency and the simplicity of the implemented patterns.

By combining computational theory with practical implementation, this project clearly illustrates the applicability and effectivenes of lexical analysis through automata and regular expresions.


## Models

In this section we analyze the two main models used in our language analysis: **Deterministic Finite Automata (DFA)** and **Regular Expressions**. Both form the backbone of our approach and offer unique advantages for representing and analyzing language patterns.

### Regular Expression

The regular expression was derived by considering the restrictions of the language and all valid combinations:

```regex
(?!.*1101|.*1122|.*1011|.*1012)[012]+
```

Let's break it down to understand how it represents our language pattern:

- **`(?!...)`**:  
  This is a **negative lookahead assertion**, which ensures that the string does **not** contain any of the forbidden patterns.

- **`.*1101|.*1122|.*1011|.*1012`**:  
  Within the lookahead, each part specifies that any number of characters (represented by `.*`) can precede a forbidden sequence. The `|` operator separates the disallowed cases.

- **`[012]+`**:  
  This allows any combination of the digits `0`, `1`, and `2`. The `+` indicates that at least one such character must be present.

Thus, the expression ensures that strings composed of digits `0`, `1`, and `2` are accepted **only if they do not** contain the sequences `1101`, `1122`, `1011`, or `1012`. If any of these occur the lookahead fails and the expression does not match.

**To run the regular expression script**:

```bash
python regex_python.py
```
Sample interaction:
```bash
Enter a string composed of 0, 1, and 2: 012
The input string '012' matches the language syntax.

Enter a string composed of 0, 1, and 2: exit
```
### DFA

Once the regular expression was fully defined, we explored its equivalent DFA. We began by identifying the five formal components that define a deterministic model. To construct the state diagram, we started with smaller sub-expressions based on the forbiden patterns and expanded from there.
This led to the creation of the final automaton diagram, which visually represents all valid transitions and the rejections for each disallowed sequence.

The graphic above shows the resulting DFA, ilustrating how the automaton navigates through states while avoiding the restricted sequences. This model was implemented in Prolog, and its behavior was verified through a comprehensive test suite (see test_automata.pl).

![image](https://github.com/user-attachments/assets/26f07407-9ac4-4c07-9df5-3abde2f75039)

**To run the DFA expression script**
```bash
swipl
?-load_files('main.pl').
?-load_files('automata.pl').
```
In the case the string is valid: 

```bash
?- validate([1,1,1,1]).
true.
```

In the case the string is not valid: 

```bash
?- validate([1,0,1,1]).
false.
```
## Tests

In this section, we will explain how automated tests were performed to verify that both the deterministic finite automaton (DFA) implemented in Prolog and the regular expresion implemented in Python function correctly according to the project requirements.

### Automaton Tests (Prolog)

The automaton tests were implemented in the `test_automata.pl` file. This file contains a series of rules and queries designed to automatically verify whether the automaton correctly accepts valid strings and rejects invalid strings according to the defined constraints.

To run these tests, follow these steps:

**1. Start SWI-Prolog from the terminal:**

```bash
swipl
```
**2. Load the main PL file and then the test file:**
```bash
?- [main].
true.

?- [test_automata].
true.
```
**3. Run the automated tests using the defined rule run_tests and the expected response is true.**
```bash
?- run_tests.
true.
```

### Pruebas de la Expresión Regular (Python)

Regular expression tests were performed using Python in the test_regex.py file. This file implements test cases using the standard unittest module, automatically verifying that the regular expresion correctly recognizes valid strings and rejects those containing prohibited sequences.

To run these tests, follow these steps:

**1. From the terminal, make sure you're in the directory where test_regex.py is located. Then run:**
```bash
python test_regex.py
```
Expected response:

You will see a structured output like this:
```bash
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```

## Analysis

The following presents a detailed time complexity analysis of both approaches used in the project: the Deterministic Finite Automaton (DFA) implemented in Prolog and the regular expression implemented in Python, We will also compare these solutions to clearly illustrate the advantages of each method.

### DFA Complexity (Prolog)

The time complex of the deterministic finite automaton implemented in Prolog can be determined by observing the recursive structure of the `parse_list` predicate. For this analysis we will use an inductive approach:

- **Initialization:**
During automaton initialization, we establish the initial state and the list to be evaluated. This process is imediate and has a constant time complexity of **O(1)**

- **Base cases:**
When the list is empty (`parse_list(State, [])`), we simply check whether the current state is valid or not. This check is immediate and also has constant time complexity **O(1)**

- **Recursive case:**
In the recursive operation (`parse_list(State, [Input|Rest])`), the transition between states depends only on the next input symbol. The search for the next transition (`transition(State, NextState, Input)`) also has constant time complexity **O(1)** due to Prolog's efficient rule storage. However, the function is called recursively as many times as the input string has characters. Therefore, if the string length is *n*, the final complexity can be expressed as:

T(n) = O(1) + T(n-1)

Solving this recursion results in a final complexity of **O(n)**, where *n* is the length of the input string.

In summary, altough the automaton has constant operations for each individual step, the recursive procedure generates a total complexity that is linear with respect to the input length.

---

### Regular Expression Complexity (Python)

The time complex of validating strings using regular expressions in Python can be analyzed as follows:

- **Initial Evaluation:**
Initially determining whether a string matches the defined general pattern is a simple operation, performed immediately by the Python standard library (`re`), which is considered constant time **O(1)**

- **String Scanning:**
The main evaluation involves examining each character in the string to check for a match with the defined pattern. Since the regular expression contains a fixed and constant number of forbidden sequences (independent of the string length) this process takes a time proportional to the total length of the input string (**O(n)**)

Since each character is inspected exactly once in the worst case, the evaluation complexity is directly expressed as **O(n)** where *n* is the length of the string.

---

### Comparison between both approaches

Both approaches have the same linear time complexity **O(n)** with respect to the size of the input string. However, there are practical differences to consider:

- The **DFA implemented in Prolog** offers deterministic and transparent analysis, facilitating logical debugging and providing clarity about the specific steps taken by the automaton.
- The **Regular Expression in Python**, although also linear in complexity, offers a more compact and efficient implementation in terms of code write, but can become less transparent when debugging complex patterns.

In conclusion, both the DFA approach in Prolog and the regular expression approach in Python offer linear **O(n)** runtimes, but the choice of method will depend on the clarity, development efficiency, and maintainability requirements of each specific project.


## Personal Conclusion

After implementing and analyzing both options, I observed that they lead to very similar results, both the regular and ADF.
Automata is particularly advantageous to me because it offers a structured approach to defining state transitions and constraints, offering flexibility to handle a wider range of patterns and constraints, including more complex rules. In many cases, automata can offer better performance compared to regular expressions, especially for larger input sizes or more complex patterns. However, my contention is that their implementation takes longer and requires more effort, and they are done in Prolog, which is more complex.

Regular expressions are like Python: simple, fast, and easy to use, especially in a simple program like the one we implemented. However, this lacks the advantages of ADF: a structured approach to defining state transitions and constraints, offering flexibility to manage a wider range of patterns and constraints, including more complex rules.

If we consider the complexity of the project, the best option for me would be regular expression due to its ease and speed, but if in the future the program needs scalability or an extension/improvement, I prefer ADF.

### References 
Moreno, F. (2023). Tema 3: Autómatas finitos. Recuperado de https://www.uhu.es/francisco.moreno/gii_mac/docs/Tema_3.pdf
GeeksforGeeks. (2021, 3 de enero). Python – Regex Lookahead. GeeksforGeeks. https://www.geeksforgeeks.org/python-regex-lookahead/
Garrido, P. M. (s.f.). Lexical_Analysis [Repositorio en GitHub]. https://github.com/paolamgarrido/Lexical_Analysis
