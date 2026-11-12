# Report fragments (Custom Question Bank)

The report is written per person in `.tex` and unified later. These fragments are
ready to be included from the main report; they contain no preamble and no
`\usepackage` commands.

## Include from the main report

```latex
\input{report/custom_question_bank}
...
\appendix
\input{report/custom_ltl_appendix}
```

## Preview PDF

`custom_report_preview.tex` is a standalone wrapper used only to compile
`PLCGen_Custom_Question_Bank.pdf`. Do not include the wrapper in the main report.

## Notes

- The fragments use only standard LaTeX (`section`, `tabular`, `itemize`).
- No internal group roles or work-division references are included.
- The dataset paths are relative to the repository root.
