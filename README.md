# How to use the CLI

The CLI works with Click. 
Provide the options, followed by the arguments. 
For example: 
```
creditcard get-results --data-path 'data/creditcard.csv' --model-version 1

```

Be aware that underscores cannot be used with the click decorator. 
Therefore, use a dash instead of an underscore.
