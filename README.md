# E1-Implementation-of-Lexical-Analysis-Automaton-and-Regular-Expression-

## Description

Lexical analysis, within the field of computational methods, is fundamental to recognizing and validating strings belonging to specific languages. This project aims to design and implement an automaton capable of correctly identifying strings generated solely by combinations of the digits **0**, **1**, and **2**, under certain specific restrictions: the strings **must not contain** the sequences `'1101'`, `'1122'`, `'1011'`, or `'1012'`. Accurat identification of these restricted patterns is crucial to ensuring the integrity of the lexical analysis.

To solve this challenge, two complementary approaches were employed. 

First, a **Deterministic Finite Automaton (DFA)** was used—an ideal mathematical tool for recognizing specific languages thanks to its defined and deterministic transition capability. A DFA is composed of five essential elements:

- **Q**: Finite set of states.  
- **Σ**: Finite set of input symbols (alphabet).  
- **δ**: Transition function that clearly specifies the next state given an input and a current state.  
- **q₀**: Initial state from which the analysis begins.  
- **F**: Set of acceptance states, where the string is considered valid.  

This automaton was implemented using **Prolog**, taking advantage of its robustness in logical representation and efficient handling of defined transition rules.

In parallel, language validation was addressed using **regular expressions**, implemented in **Python** with the `re` module. Regular expressions offer a compact and eficient method for describing textual patterns and allow rapid verification of the validity of generated strings. Because there is a direct correspondence between regular expressions and finite automata, both methods are comparable and complementary.

Finally, to ensure the accuracy and robustness of the developed system, **two complete sets of automated tests** were created. These provide empirical evidence on the effectivenes of both implementations, highlighting aspects such as computational efficiency and the simplicity of the implemented patterns.

By combining computational theory with practical implementation, this project clearly illustrates the applicability and effectiveness of lexical analysis through automata and regular expressions.


## Models

In this section, we analyze the two main models used in our language analysis: **Deterministic Finite Automata (DFA)** and **Regular Expressions**. Both form the backbone of our approach and offer unique advantages for representing and analyzing language patterns.

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

Thus, the expression ensures that strings composed of digits `0`, `1`, and `2` are accepted **only if they do not** contain the sequences `1101`, `1122`, `1011`, or `1012`. If any of these occur, the lookahead fails and the expression does not match.

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

Once the regular expression was fully defined, we explored its equivalent DFA. We began by identifying the five formal components that define a deterministic model. To construct the state diagram, we started with smaller sub-expressions based on the forbidden patterns and expanded from there, following recommendations by Michael Sipser.

This led to the creation of the final automaton diagram, which visually represents all valid transitions and the rejections for each disallowed sequence.

The graphic above shows the resulting DFA, illustrating how the automaton navigates through states while avoiding the restricted sequences. This model was implemented in Prolog, and its behavior was verified through a comprehensive test suite (see test_automata.pl).

![image](https://github.com/user-attachments/assets/26f07407-9ac4-4c07-9df5-3abde2f75039)


