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

Files under `src/` can and must be used inside

``` LATEX
\begin{document}
  ...
\end{document}
```

and not inside the preamble. These files mainly exists to eliminate boilerplate code.

## Disclaimer

These files were created to work with `LuaHBTeX, Version 1.14.0 (TeX Live 2022/dev/Debian)`. There is no guarantee that these files work with other versions or other drivers. You may want to have a look at `.vscode/settings.json` for an implementation into [VS Code] with the [LaTeX workshop extension].

The required packages can be installed by running:

```bash
apt-get --yes install texlive-latex-extra texlive-luatex texlive-lang-european texlive-science texlive-bibtex-extra biber
```

[VS Code]: https://code.visualstudio.com/
[LaTeX workshop extension]: https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop
