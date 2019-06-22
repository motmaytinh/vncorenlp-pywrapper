## vncorenlp-wrapper
[![PyPI](https://img.shields.io/pypi/v/stanfordcorenlp.svg)]()
[![GitHub release](https://img.shields.io/github/release/Lynten/stanford-corenlp.svg)]()
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/stanfordcorenlp.svg)]()


`vncorenlp-wrapper` is a Python wrapper for [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP). It provides a simple API for text processing tasks such as Tokenization, Part of Speech Tagging, Named Entity Reconigtion, Constituency Parsing, Dependency Parsing.

## Prerequisites
Java 1.8+ (Check with command: `java -version`) ([Download Page](http://www.oracle.com/technetwork/cn/java/javase/downloads/jdk8-downloads-2133151-zhs.html))

VnCoreNLP ([Download Page](https://github.com/vncorenlp/VnCoreNLP))

Py4j ([Download Page](https://www.py4j.org/download.html))

## Installation

Clone this repository, then put VnCoreNLP-1.1.jar and models directory of VnCoreNLP in the same working folder.

## Example
### Simple Usage
```python
# Simple usage
from vncorenlp import VnCoreNLP

# simple usage
nlp = VnCoreNLP("/home/workspace/tokenizer/VnCoreNLP-1.1.jar")

sentence = 'xin chào các bạn!'

tokens = nlp.word_tokenizer(sentence)

print(tokens)
```

Output format:
```python
# Tokenize
['xin', 'chào', 'các', 'bạn', '!']

```