
# List of commands

A script is a list of commands and the data they need. The commands are shown below on separate lines,
but the executor knows what inputs goes with which commands.

```json
[
  "assert_second_noun_is","LAMP",
  "swap_objects","CANDLE","LITCANDLE",
  "print","THE CANDLE IS NOW BURNING"
]
```

# Assertions

Several commands assert that a condition is true. If the condition IS true, then the script continues to the next command.
If the condition is NOT true, then the current script is aborted with a FAIL status. A script get a PASS status if all commands
execute with no failed assertion.

## Assert All Pass

This construct is used to define subscripts. The executor groups all of the commands in the subscript together and runs them.
If they all pass, this command returns PASS. If any fail, this command returns FAIL.

```json
[
  "assert_all_pass", []
]
```

## Assert One Passes

This construct runs the commands in a script one by one until one passes. It expects (hopes) that one will pass. As soon as a command 
passes, the subscript is aborted and this command returns PASS. If all of the commands fails, this command returns FAIL.

```json
[
  "assert_one_passes", []
]
```

# Switch

This is a commonly used construct for selecting one passing assertion and running its script. This can be implemented
with "assert_one_passes" and "assert_all_passes", but this construct is syntactically easier.

The "switch" command has two data items: the assertion command to check at every case and a list of cases.

Each case is a list of values (usually one, but sometimes more) to be passed into the assertion command followed by the script to run 
if the assertion is true.

Only the script of the first passing case is executed. The result of that script, PASS or FAIL, is returned from the command.
If there are no passing cases then the command returns FAIL.

```json
[
  "switch","assert_VAR_object_is", [
      "SWORD", [],
      "KNIFE", []
  ]
]
```
