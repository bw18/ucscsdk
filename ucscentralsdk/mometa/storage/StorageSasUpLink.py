"""This module contains the general information for StorageSasUpLink ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class StorageSasUpLinkConsts():
    CONTROLLER_TYPE_FLASH = "FLASH"
    CONTROLLER_TYPE_HBA = "HBA"
    CONTROLLER_TYPE_NVME = "NVME"
    CONTROLLER_TYPE_PCH = "PCH"
    CONTROLLER_TYPE_PT = "PT"
    CONTROLLER_TYPE_SAS = "SAS"
    CONTROLLER_TYPE_SATA = "SATA"
    CONTROLLER_TYPE_SD = "SD"
    CONTROLLER_TYPE_EXTERNAL = "external"
    CONTROLLER_TYPE_UNKNOWN = "unknown"
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"
    LINK_SPEED_1_5_GBPS = "1-5-gbps"
    LINK_SPEED_12_GBPS = "12-gbps"
    LINK_SPEED_3_GBPS = "3-gbps"
    LINK_SPEED_6_GBPS = "6-gbps"
    LINK_SPEED_DISABLED = "disabled"
    LINK_SPEED_DOWN = "down"
    LINK_SPEED_HOST_POWER_OFF = "host-power-off"
    LINK_SPEED_UNKNOWN = "unknown"
    LINK_SPEED_UNSUPPORTED_DEVICE = "unsupported-device"


class StorageSasUpLink(ManagedObject):
    """This is StorageSasUpLink class."""

    consts = StorageSasUpLinkConsts()
    naming_props = set([u'serverId', u'controllerType', u'controllerId', u'id'])

    mo_meta = MoMeta("StorageSasUpLink", "storageSasUpLink", "sas-uplink-server-[server_id]-controller-[controller_type]-[controller_id]-id-[id]", None, "InputOutput", 0xff, [], ["read-only"], [u'storageSasExpander'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "controller_id": MoPropertyMeta("controller_id", "controllerId", "uint", None, MoPropertyMeta.NAMING, 0x2, None, None, None, [], []), 
        "controller_type": MoPropertyMeta("controller_type", "controllerType", "string", None, MoPropertyMeta.NAMING, 0x4, None, None, None, ["FLASH", "HBA", "NVME", "PCH", "PT", "SAS", "SATA", "SD", "external", "unknown"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", None, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "link_descr": MoPropertyMeta("link_descr", "linkDescr", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["1-5-gbps", "12-gbps", "3-gbps", "6-gbps", "disabled", "down", "host-power-off", "unknown", "unsupported-device"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "server_id": MoPropertyMeta("server_id", "serverId", "uint", None, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "controllerId": "controller_id", 
        "controllerType": "controller_type", 
        "dn": "dn", 
        "id": "id", 
        "lc": "lc", 
        "linkDescr": "link_descr", 
        "linkSpeed": "link_speed", 
        "rn": "rn", 
        "serverId": "server_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, server_id, controller_type, controller_id, id, **kwargs):
        self._dirty_mask = 0
        self.server_id = server_id
        self.controller_type = controller_type
        self.controller_id = controller_id
        self.id = id
        self.child_action = None
        self.lc = None
        self.link_descr = None
        self.link_speed = None
        self.status = None

        ManagedObject.__init__(self, "StorageSasUpLink", parent_mo_or_dn, **kwargs)
