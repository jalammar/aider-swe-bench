# A no-op patch which creates an empty file is used to stand in for
# the `model_patch` and/or `test_patch` when running SWE Bench tests
# without one or both of those patches.
def run_tests(entry, model_patch=None, use_test_patch=False, model_name_or_path="none"):
    """
    Run tests for the SWE Bench `entry`, optionally applying a `model_patch` first.

    If `use_test_patch` is True, then also apply the `test_patch` to bring in
    the tests which determine if the issue is resolved. So False means
    only run the tests that existed at the `base_commit` and any new/changed
    tests contained in the `model_patch`.

    Optionally specify a `model_name_or_path`, which isn't really used since
    the log_dir for the tests is a temp dir which is discarded.
    """
    # Use a no-op patch if no model_patch is provided
    # Use a no-op patch if use_test_patch is False
    if use_test_patch: