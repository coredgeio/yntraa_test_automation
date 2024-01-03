import pytest

class ComputePageLocators:
    COMPUTE_TAB = "//a[text()='Compute']"
    HEADER = "//h1[contains(text(), 'Compute Home Screen')]"
    CREATE_VM_BUTTON = "//button[contains(text(), 'Create Virtual Machine')]"

class CreateVirtualMachinePageLocators:
    HEADER = "//h1[contains(text(), 'Create Virtual Machine')]"
    MACHINE_NAME_INPUT = "//input[@id='machine_name']"
    AVAILABILITY_ZONE_DROPDOWN = "//select[@id='availability_zone']"
    CREATE_BUTTON = "//button[contains(text(), 'Create')]"

