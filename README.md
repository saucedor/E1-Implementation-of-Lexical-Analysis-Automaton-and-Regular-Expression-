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





