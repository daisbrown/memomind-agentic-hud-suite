# local-rag-whisper-cue

A local, deterministic ADR-ID trigger and lookup, with no microphone, embeddings, LanceDB or vector retrieval. Example content is fictional; no latency target has been measured.

Run from the repository root after installing the core:

```sh
python projects/06-local-rag-whisper-cue/simulate_arch_call.py
```

Example frame from the replay:

```text
+----------------------------------+
|                                  |
|                                  |
|                                  |
+----------------------------------+
```

`local_index.py` provides a small local lexical index of Markdown files; it is not vector retrieval.
