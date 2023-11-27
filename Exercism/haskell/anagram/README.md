# Anagram

Welcome to Anagram on Exercism's Haskell Track.
If you need help running the tests or submitting your code, check out `HELP.md`.

## Instructions

An anagram is a rearrangement of letters to form a new word: for example `"owns"` is an anagram of `"snow"`.
A word is not its own anagram: for example, `"stop"` is not an anagram of `"stop"`.

Given a target word and a set of candidate words, this exercise requests the anagram set: the subset of the candidates that are anagrams of the target.

The target and candidates are words of one or more ASCII alphabetic characters (`A`-`Z` and `a`-`z`).
Lowercase and uppercase characters are equivalent: for example, `"PoTS"` is an anagram of `"sTOp"`, but `StoP` is not an anagram of `sTOp`.
The anagram set is the subset of the candidate set that are anagrams of the target (in any order).
Words in the anagram set should have the same letter case as in the candidate set.

Given the target `"stone"` and candidates `"stone"`, `"tones"`, `"banana"`, `"tons"`, `"notes"`, `"Seton"`, the anagram set is `"tones"`, `"notes"`, `"Seton"`.

To complete this exercise you need to implement the function `anagramsFor`,
that takes a *word* and a group of *words*, returning the ones that are
anagrams of the given *word*.

If it is your first time solving this exercise, it is recommended that you
stick to the provided signature:

```haskell
anagramsFor :: String -> [String] -> [String]
```

Later, it may be a good idea to revisit this problem and play with other data
types and libraries:

- `Text`, from package *text*.
- `Sequence` and `Set`, from package *containers*.
- `MultiSet`, from package *multiset*

The test suite was intentionally designed to accept almost any type signature
that makes sense, so you are encouraged to find the one you think is the best.

## Source

### Created by

- @etrepum

### Contributed to by

- @gris
- @iHiD
- @kytrinyx
- @mttakai
- @petertseng
- @ppartarr
- @rbasso
- @sshine
- @tejasbubane

### Based on

Inspired by the Extreme Startup game - https://github.com/rchatley/extreme_startup