def is_report_safe(levels: list[int]):
    diffs = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
    return all(abs(diff) <= 3 for diff in diffs) and (
            all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs))


def count_safe_reports(reports: list[str]) -> int:
    safe_reports = 0
    for report in reports:
        levels = list(map(int, report.split(" ")))
        if is_report_safe(levels):
            safe_reports += 1
    return safe_reports


def is_report_safe_with_dampener(levels: list[int]):
    if is_report_safe(levels):
        return True
    else:
        for i in range(len(levels)):
            levels_copy = levels[:i] + levels[i + 1:]
            if is_report_safe(levels_copy):
                return True
    return False

def count_safe_reports_with_dampener(reports: list[str]) -> int:
    safe_reports = 0
    for report in reports:
        levels = list(map(int, report.split(" ")))
        if is_report_safe_with_dampener(levels):
            safe_reports += 1
    return safe_reports