
1. Setup

```
python -m venv .venv
source .venv/bin/activate
pip install inspect-ai
```

2. Run eval, and interrupt it with ctrl+c

```
inspect eval example.py --model mockllm/model
```

The output will look something like

```
Task interrupted (85 of 1,000 total samples logged before interruption). Resume task with:                                                        
                                                                                                                                                  
inspect eval-retry logs/some-log-filename.eval   
```

3. Retry the eval

```
inspect eval-retry logs/replace-with-your-log-filename.eval
```

**Expected behavior**: Successful run.

**Actual behavior**: Error is thrown

```
Traceback (most recent call last):
  File "/Users/jeqcho/inspect-bug-reducer/.venv/bin/inspect", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_cli/main.py", line 56, in main
    inspect(auto_envvar_prefix="INSPECT")  # pylint: disable=no-value-for-parameter
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/click/core.py", line 1442, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/click/core.py", line 1363, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/click/core.py", line 1830, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/click/core.py", line 1226, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/click/core.py", line 794, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_cli/common.py", line 45, in wrapper
    return cast(click.Context, func(*args, **kwargs))
                               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_cli/common.py", line 110, in wrapper
    return cast(click.Context, func(*args, **kwargs))
                               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_cli/eval.py", line 1247, in eval_retry_command
    eval_retry(
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_eval/eval.py", line 830, in eval_retry
    return task_display().run_task_app(run_task_app)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_display/textual/display.py", line 51, in run_task_app
    raise result.value
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/textual/worker.py", line 368, in _run
    self._result = await self.run()
                   ^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/textual/worker.py", line 352, in run
    return await (
           ^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/textual/worker.py", line 339, in _run_async
    return await self._work
           ^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_eval/eval.py", line 804, in run_task_app
    return await eval_retry_async(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_eval/eval.py", line 972, in eval_retry_async
    Epochs(eval_log.eval.config.epochs, eval_log.eval.config.epochs_reducer)
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_eval/task/epochs.py", line 21, in __init__
    self.reducer = create_reducers(reducer)
                   ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/scorer/_reducer/registry.py", line 156, in create_reducers
    return [
           ^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/scorer/_reducer/registry.py", line 157, in <listcomp>
    r if isinstance(r, ScoreReducer) else create_reducer(r) for r in reducers
                                          ^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/scorer/_reducer/registry.py", line 148, in create_reducer
    Callable[..., ScoreReducer], registry_create("score_reducer", name)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jeqcho/inspect-bug-reducer/.venv/lib/python3.11/site-packages/inspect_ai/_util/registry.py", line 347, in registry_create
    raise LookupError(f"{name} was not found in the registry")
LookupError: a_custom_score_reducer was not found in the registry
```

