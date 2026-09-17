# Use Loka with Gemini

A pasted GitHub URL is not a reliable way to give Gemini a repository. Use one
of these paths instead.

## Evaluate or use the whole repository

On Gemini web on a computer:

1. Select **Add file**.
2. Select **More uploads**.
3. Select **Import code**.
4. Paste `https://github.com/Wazifati/loka-context-harness`.
5. Complete the import, then tell Gemini the task and the Loka route you want.

Gemini imports a repository snapshot. If the repository changes, import it
again for a current review. After import, you can continue that conversation in
the Gemini web or mobile app.

Google documents the current Import code flow here: <https://support.google.com/gemini/answer/16176929>.

For an accurate evaluation, start with the grounded prompt in
[`EVALUATE_LOKA.md`](../EVALUATE_LOKA.md).

## Do one research task without importing the repository

Attach [`DEEP_RESEARCH_START.md`](../DEEP_RESEARCH_START.md) to a Gemini chat,
then state the research task. This avoids asking Gemini to browse repository
folders or retrieve multiple files.

If Gemini Deep Research is available in your account, enable it for current
web research. Loka shapes the work; it does not supply browsing or source
access where Gemini does not have it.

## Create a reusable personal Gem

On Gemini web, create a new Gem and add `DEEP_RESEARCH_START.md` under its
Knowledge files. Put the following in its instructions:

```text
Use the attached Loka Deep Research protocol for every research task.
State material assumptions, distinguish evidence from inference, and never
claim source access you did not have. Produce a decision-ready report.
```

You can then use the Gem from Gemini web or mobile. If your Gemini account
allows sharing, you may share the Gem with people who should be able to view
its instructions and attached file. Review sharing and file-access settings
before making a Gem public.
