import tempfile
def run_tests(entry, model_patch = None, use_new_tests=False, model_name_or_path="none"):
    instance_id = entry["instance_id"]
    test_type = MAP_REPO_TO_TEST_FRAMEWORK[entry["repo"]]
    test_directives = get_test_directives(entry)
    if not model_patch:
        model_patch = NOOP_PATCH.format(nonce="model_patch")

    if use_new_tests:
        test_patch = entry['test_patch']
    else:
        test_patch = NOOP_PATCH.format(nonce="test_patch")

    entry_instance = {
        "repo": entry["repo"],
        "version": entry["version"],
        "base_commit": entry["base_commit"],
        "instance_id": entry["instance_id"],
        "model_name_or_path": model_name_or_path,
        "model_patch": model_patch,
        "test_patch": test_patch,
    log_dir = tempfile.TemporaryDirectory(dir="/tmp").name
    dump(log_dir)

        run_docker_evaluation(entry_instance, namespace, log_dir, timeout, log_suffix)
    log_fname = Path(log_dir) / f'{instance_id}.{model_name_or_path}.eval.log'
    passed = '>>>>> All Tests Passed' in log_text

    return passed, log_text


def main():
    from harness import get_dataset

    dataset = get_dataset()


    pred_path = "predictions/oracle-openrouter--anthropic--claude-3-opus.jsonl"
    predictions = [json.loads(line) for line in open(pred_path)]

    num = 0
    num_passed = 0

    instance_ids = sys.argv[1:]

    for entry in dataset.values():
        if instance_ids and entry['instance_id'] not in instance_ids:
            continue

        passed, test_text = run_tests(entry)
        num += 1
        if passed:
            num_passed += 1
        dump(num_passed/num)
if __name__ == '__main__':
    status = main()
    sys.exit(status)