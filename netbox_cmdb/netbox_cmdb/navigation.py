"""Navigation (menu)."""

from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_cmdb:asn_list",
        link_text="AS Numbers",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:asn_add",
                title="AS Numbers",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:bgpsession_list",
        link_text="BGP Sessions",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:bgpsession_add",
                title="BGP Sessions",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:bgppeergroup_list",
        link_text="BGP Peer Groups",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:bgppeergroup_add",
                title="BGP Peer Groups",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:routepolicy_list",
        link_text="Route Policies",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:routepolicy_add",
                title="Route Policies",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:snmp_list",
        link_text="SNMP",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:snmp_add",
                title="SNMP",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:snmpcommunity_list",
        link_text="SNMP Community",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:snmpcommunity_add",
                title="SNMP Community",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:deviceinterface_list",
        link_text="Device Interfaces",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:deviceinterface_add",
                title="Device Interfaces",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:logicalinterface_list",
        link_text="Logical Interfaces",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:logicalinterface_add",
                title="Logical Interfaces",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:vrf_list",
        link_text="VRFs",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:vrf_add",
                title="VRFs",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:vlan_list",
        link_text="VLANs",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:vlan_add",
                title="VLANs",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_cmdb:link_list",
        link_text="Links",
        buttons=(
            PluginMenuButton(
                link="plugins:netbox_cmdb:link_add",
                title="Links",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
)
