
import pytest
class LoginRequirements:

    URL = "https://console-revamp-sbx.yntraa.com"
    USERNAME = "mailto:priti.ltd@yopmail.com"
    PASSWORD = "India@143"
    HOME_PAGE_HEADER = "//h3[normalize-space()='Enabling Possibilities. Empowering Ideas.']"
    HOME_PAGE_DECSRP = "//p[contains(text(),'Discover the power of our public cloud platform')]"

class ComputePageLocators:

    COMPUTE_TAB = "//a[text()='Compute']"
    COMPUTE_HEADER = "//h3[normalize-space()='Compute']"
    COMPUTE_DESCRP = "(//h3[normalize-space()='Compute']//following::p)[1]"
    COMPUTE_CREATE_BUTTON = "//button[normalize-space()='Create']"
    STORAGE_TAB = "//a[text()='Storage']"
    NETWORKING_TAB = "//a[text()='Networking']"
    SECURITY_TAB = "//a[text()='Security']"
    AUTOMATION_TAB = "//a[text()='Automation']"


class TejasComputeLocators:

    TEJAS_COMPUTE_TAB = "//p[text()='Tejas Compute']" #no data-testid
    TEJAS_HEADER = "//h3[normalize-space()='Tejas Compute']"
    TEJAS_DESCRP = "//p[contains(text(),'Virtual Machines are virtualized computing instances that allow users to run applications and services in a cloud environment.')]"
    LEARN_MORE = "//button[text()='Learn more']"
    CREATE_VM_BUTTON = "//button[@data-testid='compute-btn-create']"
    CREATE_VM_HEADER = "//h5[normalize-space()='Create Virtual Machine']"
    CREATE_VM_DESCRP = "//p[contains(text(),'Virtual machines (VMs) are software-based emulations of physical computers.')]"
    MACHINE_DETAILS_HEADER = "//h6[normalize-space()='Machine Details']"
    MACHINE_DETAILS_DESCRP = "//p[normalize-space()='Choose a friendly name for your virtual machine.']"
    NAME_FIELD = "//input[@id='instance_name']"
    NAME_FIELD_LABEL = "//input[@placeholder='Please enter a name']"
    AVAILABILITY_ZN_HEADER = "//h6[normalize-space()='Choose Availability Zone']"
    AVAILABILITY_ZN_DESCRP = "//p[contains(text(),'An availability zone is a physically separate data')]"
    AVAILABILITY_ZN_DROPDOWN = "//input[@id='availability_zone']"
    CHOOSE_IMAGE = "//h6[normalize-space()='Choose an Image']"
    CHOOSE_IMG_HEADER = "//p[contains(text(),'Image refers to a pre-configured snapshot or templ')]"
    PUBLIC_IMAGE = "//button[@data-testid='public-images-tab']"
    SNAPSHOT = "//button[@data-testid='snapshots-tab']"
    IMAGE_SEARCH = "//input[@id=':r1d:']"
    VERSION_DROPDOWN = "//input[@id='image_id']"
    CHOSE_FLAVOR_HEADER = "//h6[normalize-space()='Choose Flavor']"
    CHOSE_FLAVOR_DESCRP = "//p[contains(text(),'A flavor refers to a predefined combination of vir')]"
    #ADD ONE FOR FLAVORS AS WELL
    FLAVOR_ONE = "//span[contains(text(),'m1.amphora')]"
    ROOT_VOLUME_HEADER = "//h6[normalize-space()='Root Volume']"
    ROOT_VOLUME_DESCRP = "//p[contains(text(),'Root volumes are block storage devices that provid')]"
    ROOT_VOLUME_TYPE = "//input[@id='volume_type']"
    ROOT_VOLUME_DECREASE = "//button[1][@data-testid='root-volume-in-gi-b-count']"
    ROOT_VOLUME_INCREASE = "//button[2][@data-testid='root-volume-in-gi-b-count']"
    MACHINE_CREDENTIALS_HEADER = "//h6[normalize-space()='Your Machine Credentials']"
    MACHINE_CREDENTIALS_DESCRP = "//p[contains(text(),'Select a key pair or username & password for conne')]"
    CREDENTIALS_KEY_PAIR_OPTION = "//button[@data-testid='key-pair-tab']"
    CREDENTIALS_USER_PASS_OPTION = "//button[@data-testid='username-password-tab']"
    KEY_PAIR_DROPDOWN = "//input[@id='keypair_id']"
    CHOOSE_NETWORK_HEADER = "//h6[normalize-space()='Choose Networks']"
    CHOOSE_NETWORK_DESCRP = "//p[contains(text(),'A network refers to a virtual network that connect')]"
    NETWORKS = "//input[@id='network_id']" # might need to update again
    CHOOSE_SECURITY_GRP_HEADER = "//h6[normalize-space()='Choose Security Groups']"
    CHOOSE_SECURITY_GRP_DESCRP = "//p[contains(text(),'Security Groups are virtual firewalls that control')]"
    SECURITY_GROUPS = "//input[@id='sec_group_id']" # might need to update again
    MACHINE_BACKUP_HEADER = "//h6[normalize-space()='Machine Backup']"
    MACHINE_BACKUP_DESCRP = "//p[contains(text(),'Backups automatically create weekly copies of your')]"
    ENABLE_BACKUP_CHECKBOX = "//span[@data-testid='enable-virtual-machine-backup-checkbox']"
    ADD_LABELS_HEADER = "//h6[normalize-space()='Add Labels']"
    ADD_LABELS_DESCRP = "//p[text()='You can add upto 5 labels']"
    CREATE_VM_SUMMARY = "//h6[normalize-space()='Summary']"
    CANCEL_BUTTON = "//button[contains(text(),'Cancel')]"
    FINAL_CREATE_VM_BUTTON = "//button[@data-testid='confirm']//div[text()='Create']"



