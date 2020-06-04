# Count the words in an input string

## Input

This function takes a single string as an argument.

```
Hello, my cat. And my cat doesn't say "hello" back.
```

## Output

It returns a dictionary of words and their counts:

```
{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
```

Case should be ignored. Output keys must be lowercase.

Key order in the dictionary doesn't matter.

Split the strings into words on any whitespace.

Ignore each of the following characters:

```
" : ; , . - + = / \ | [ ] { } ( ) * ^ &
```

If the input contains no ignored characters, return an empty dictionary.

"""
I wrote a function to populate the possible range (domain) of inputs using the existing slow function and saved it to a json file. Then in the fast one I just read in the json file and pull the values out of dict produced by it - there aren't actually that many possible combinations so it's pretty fast to pre-populate it and extremely fast to just read the values out of the object.

Alex Gohorel < 1 minute ago
The reason the test is so slow is because it's repeatedly calling the same combination of inputs, but there are only something like 20ish possible combinations. I think you could also build your cache as you go, then you don't need to pre-populate a static file.
"""
