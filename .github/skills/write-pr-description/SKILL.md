---
name: write-pr-description
description: "Write or update rainfall pull request descriptions and PR bodies. Use when drafting, opening, or editing a pull request, summarising a branch for review, or completing the PR checklist."
---

# Write a pull request description

## Gather evidence

1. Read `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` at the repository root.
2. Confirm the intended base repository, base branch, head repository and head
   branch. Inspect the remotes rather than assuming that a fork's upstream is
   the target. When the user requests a fork-only PR, target the fork explicitly.
3. Inspect the commits and complete diff between the base and head. Describe
   only changes in that diff; do not include unrelated local work.
4. Read `.github/pull_request_template.md` and check
   `.github/PULL_REQUEST_TEMPLATE/` for applicable templates. Use the selected
   template verbatim as the structure: preserve headings, comments, checklist
   text and ordering. Replace placeholders with evidence-based details.

## Draft the body

1. Under `Summary`, explain the problem, the behaviour change and why the fix
   works. Include related documentation, regression tests and any limitations.
   Use concise British English.
2. Reference the issue with its correct repository. Use `#number` only for an
   issue in the PR's target repository; otherwise use `owner/repo#number`.
   For a fork-only PR addressing an upstream issue, use `Related to` rather
   than a closing keyword, so the description does not request upstream closure.
3. Describe validation under `Summary`, without displacing template sections.
   Run the commands documented in `CONTRIBUTING.md` when feasible:
   - `ruff check .`
   - `ruff format --check .`
   - `mypy`
   - `python -m pytest`
   Record each exact command and its result, including the test count. Include
   relevant focused regression commands and distinguish expected pre-fix
   failures from final results. If a check was not run or failed, say so and
   explain why; never imply success.
4. Complete checklist items only when verified. Keep inapplicable items
   unchecked and explain why nearby. In particular, `@validate_records` applies
   to functions accepting dated records, not functions taking rainfall values.
5. Disclose Copilot assistance and confirm that new commits include an
   `Assisted-by: Copilot` trailer. Follow any other required commit trailers.
   Do not claim trailers exist without inspecting the commits.

## Review and publish

1. Check every statement against the diff, commit messages and check output.
   Do not invent issue references, test results or CI status.
2. If no repository template exists, use concise `Summary` and `Validation`
   sections, with issue references and limitations as appropriate.
3. If asked only for a draft, return the body without publishing. Otherwise,
   create or update the PR with the verified title, body and explicit target.
   Do not push, fork or change Actions settings unless authorised.
4. Verify the created PR's base and head repositories and branches. Report the
   PR link and any outstanding checks; do not equate local checks with CI.
