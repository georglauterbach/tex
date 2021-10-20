# TeX with include

## About

This repository contains files in the form of "headers" to supply someone writing with TeX with the necessary templates. Like in C or Rust, you can "include" these files in your TeX project, either by downloading them or cloning this repository as a submodule and then using `\input{}`.

The order is already given by the order of the files under `include/`. Files under `include/` can only be used in the preamble. You will need to import the language files and the file containing generic code snippets to make some of the other files work, i.e. you must include

``` LATEX
% ...

% choose your language
\input{tex/include/01-language_english}
\input{tex/include/01-language_german}
% import this one too
\input{tex/include/02-generic}

% ...

\begin{document}
```

Files under `src/` can be used inside

``` LATEX
\begin{document}
  ...
\end{document}
```

## Disclaimer

These files were created to work with XeLaTeX version `XeTeX 3.14159265-2.6-0.999992`. There is no guarantee that these files work with other versions or other drivers. You may want to have a look at `.vscode/settings.json` for an implementation into [VS Code] with the [LaTeX workshop extension].

[VS Code]: https://code.visualstudio.com/
[LaTeX workshop extension]: https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop
