import os
import unittest
from pathlib import Path

from checkov.arm.checks.resource.DataFactoryUsesGitRepository import check
from checkov.arm.runner import Runner
from checkov.runner_filter import RunnerFilter


class TestDataFactoryUsesGitRepository(unittest.TestCase):

    def test_summary(self):
        # given
        test_files_dir = Path(__file__).parent / "example_DataFactoryUsesGitRepository"

        # when
        report = Runner().run(root_folder=str(test_files_dir), runner_filter=RunnerFilter(checks=[check.id]))

        # then
        summary = report.get_summary()

        passing_resources = {
            "Microsoft.DataFactory/factories.pass",
        }
        failing_resources = {
            "Microsoft.DataFactory/factories.fail",
            "Microsoft.DataFactory/factories.fail2",
        }

        passed_check_resources = {c.resource for c in report.passed_checks}
        failed_check_resources = {c.resource for c in report.failed_checks}

        self.assertEqual(summary["passed"], len(passing_resources))
        self.assertEqual(summary["failed"], len(failing_resources))
        self.assertEqual(summary["skipped"], 0)
        self.assertEqual(summary["parsing_errors"], 0)

        self.assertEqual(passing_resources, passed_check_resources)
        self.assertEqual(failing_resources, failed_check_resources)


