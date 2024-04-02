from checkov.common.models.consts import ANY_VALUE

from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck
from typing import Any


class AppConfigSoftDelete7Days(BaseResourceValueCheck):
    def __init__(self) -> None:
        name = " Ensure 'Soft Delete' is set to 7 days"
        id = "CKV_AZURE_243"
        supported_resources = ("azurerm_app_configuration",)
        categories = (CheckCategories.BACKUP_AND_RECOVERY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return "soft_delete_retention_days"

    def get_expected_value(self) -> Any:
        return '7'


check = AppConfigSoftDelete7Days()
