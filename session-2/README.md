# Session 2

## TODO
Since today is April's Fools day, TWers suspect that there are fake news about TW. They know that the news is false if it contains any of the string(s) "unreadable/messy/badcode/lone" as a subsequence. Help TWers determine whether this piece of news is true.

INPUT : The first and only line contains a non-empty string s of length no greater than 1000, consisting of lowercase letters of Latin alphabet (a-z).

OUTPUT : Output the different SEV level based on the sum of the weighted number of unique occurrence of the string(s) "unreadable/messy/badcode/lone" as a subsequence. If none, output NOSEV

## Metric
|sum of weight | severity |
|---|---|
|1|3|
|2|2|
|2 >|1|

|bad strings| weight |
|---|---|
|lone|2|
|badcode|2|
|messy|1|
|unreadable|1|

## Test cases
| words | sum | severity |
|---|---|---|
|thoughtworkslikestowritemessycodeandcantidentifycodesmell|3|1|
|thoughtworkslikestoworkaloneandsleep|2|2|
|thoughtworkerswritegoodcode|0|NOSEV|

## Extension
If any of the following string(s) appear “pairing/tdd/agile”, decrease the count of bad words according to the number of occurrences.

|words|sum|severity|
|---|---|---|
|thoughtworkslikestowritemessycodeandcantidentifycodesmell|2|2|
|thoughtworkslikestoworkaloneandsleep|2|2|
|thoughtworkerswritegoodcode|0|NOSEV|
