sexpr
=====
An [s-expression][1] arithmetic calculator.  Because I almost bombed a phone
screening forgetting how to fiddle with the stack in the parser.

Example
-------
```console
$ python3.7 sexpr.py 
sexpr> 4.3
4.3
sexpr> (+ 2 8)
10
sexpr> (* 3 (/ 1 2))
1.5
```
Negative numbers and scientific notation are also supported.  Whatever Python's
`int` and/or `float` constructors can handle.

Operations
----------
- `(+ arg args ...)`: sum all of the arguments
- `(* arg args ...)`: multiply all of the arguments
- `(/ arg args ...)`: divide `arg` by each of `args`, i.e.
  `arg / (arg2 * arg3 * ...)`.
- `(** arg args ...)`: exponentiate to the power of each of `args` with base
  `arg`, i.e. `pow(arg, arg2 * arg3 * ...)`.

[1]: https://en.wikipedia.org/wiki/S-expression