"""URLs."""

from django.urls import path
from netbox.views.generic import ObjectChangeLogView, ObjectJournalView

from netbox_cmdb.models.bgp import ASN, BGPSession, DeviceBGPSession, BGPPeerGroup
from netbox_cmdb.models.interface import DeviceInterface, Link, LogicalInterface
from netbox_cmdb.models.route_policy import RoutePolicy
from netbox_cmdb.models.snmp import SNMP, SNMPCommunity
from netbox_cmdb.models.vlan import VLAN
from netbox_cmdb.models.vrf import VRF
from netbox_cmdb.views import (
    ASNDeleteView,
    ASNEditView,
    ASNListView,
    ASNView,
    BGPPeerGroupDeleteView,
    BGPPeerGroupEditView,
    BGPPeerGroupListView,
    BGPPeerGroupView,
    BGPSessionBulkDeleteView,
    BGPSessionDeleteView,
    BGPSessionEditView,
    BGPSessionListView,
    BGPSessionView,
    DeviceBGPSessionEditView,
    DeviceBGPSessionListView,
    DeviceBGPSessionView,
    DeviceDecommissioningView,
    DeviceBGPSessionDeleteView,
    DeviceInterfaceDeleteView,
    DeviceInterfaceEditView,
    DeviceInterfaceListView,
    DeviceInterfaceView,
    LinkDeleteView,
    LinkEditView,
    LinkListView,
    LinkView,
    LogicalInterfaceDeleteView,
    LogicalInterfaceEditView,
    LogicalInterfaceListView,
    LogicalInterfaceView,
    RoutePolicyDeleteView,
    RoutePolicyEditView,
    RoutePolicyListView,
    RoutePolicyView,
    SiteDecommissioningView,
    SNMPCommunityDeleteView,
    SNMPCommunityEditView,
    SNMPCommunityListView,
    SNMPDeleteView,
    SNMPEditView,
    SNMPListView,
    VLANDeleteView,
    VLANEditView,
    VLANListView,
    VLANView,
    VRFDeleteView,
    VRFEditView,
    VRFListView,
    VRFView,
)

urlpatterns = [
    path(
        "decommissioning/device/<int:pk>/delete",
        DeviceDecommissioningView.as_view(),
        name="device_decommissioning_delete",
    ),
    path(
        "decommissioning/site/<int:pk>/delete",
        SiteDecommissioningView.as_view(),
        name="site_decommissioning_delete",
    ),
    # ASN
    path("asn/", ASNListView.as_view(), name="asn_list"),
    path("asn/add/", ASNEditView.as_view(), name="asn_add"),
    path("asn/<int:pk>/", ASNView.as_view(), name="asn"),
    path("asn/<int:pk>/edit/", ASNEditView.as_view(), name="asn_edit"),
    path("asn/<int:pk>/delete/", ASNDeleteView.as_view(), name="asn_delete"),
    path(
        "asn/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="asn_changelog",
        kwargs={"model": ASN},
    ),
    path(
        "asn/<int:pk>/journal/",
        ObjectJournalView.as_view(),
        name="asn_journal",
        kwargs={"model": ASN},
    ),
    # BGP session
    path("bgp-session/", BGPSessionListView.as_view(), name="bgpsession_list"),
    path("bgp-session/add/", BGPSessionEditView.as_view(), name="bgpsession_add"),
    path("bgp-session/<int:pk>/", BGPSessionView.as_view(), name="bgpsession"),
    path(
        "bgp-session/<int:pk>/edit/",
        BGPSessionEditView.as_view(),
        name="bgpsession_edit",
    ),
    path(
        "bgp-session/<int:pk>/delete/",
        BGPSessionDeleteView.as_view(),
        name="bgpsession_delete",
    ),
    path("bgp-session/delete/", BGPSessionBulkDeleteView.as_view(), name="bgpsession_bulk_delete"),
    path(
        "bgp-session/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="bgpsession_changelog",
        kwargs={"model": BGPSession},
    ),
    path(
        "bgp-session/<int:pk>/journal/",
        ObjectJournalView.as_view(),
        name="bgpsession_journal",
        kwargs={"model": BGPSession},
    ),
    # Device BGP session
    path("device-bgp-session/", DeviceBGPSessionListView.as_view(), name="devicebgpsession_list"),
    path("device-bgp-session/add", DeviceBGPSessionEditView.as_view(), name="devicebgpsession_add"),
    path("device-bgp-session/<int:pk>/", DeviceBGPSessionView.as_view(), name="devicebgpsession"),
    path(
        "device-bgp-session/<int:pk>/edit",
        DeviceBGPSessionEditView.as_view(),
        name="devicebgpsession_edit",
    ),
    path(
        "device-bgp-session/<int:pk>/delete",
        DeviceBGPSessionDeleteView.as_view(),
        name="devicebgpsession_delete",
    ),
    path(
        "device-bgp-session/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="devicebgpsession_changelog",
        kwargs={"model": DeviceBGPSession},
    ),
    # Peer Group
    path("peer-group/", BGPPeerGroupListView.as_view(), name="bgppeergroup_list"),
    path("peer-group/add/", BGPPeerGroupEditView.as_view(), name="bgppeergroup_add"),
    path("peer-group/<int:pk>/", BGPPeerGroupView.as_view(), name="bgppeergroup"),
    path(
        "peer-group/<int:pk>/edit/",
        BGPPeerGroupEditView.as_view(),
        name="bgppeergroup_edit",
    ),
    path(
        "peer-group/<int:pk>/delete/",
        BGPPeerGroupDeleteView.as_view(),
        name="bgppeergroup_delete",
    ),
    path(
        "peer-group/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="bgppeergroup_changelog",
        kwargs={"model": BGPPeerGroup},
    ),
    path(
        "peer-group/<int:pk>/journal/",
        ObjectJournalView.as_view(),
        name="bgppeergroup_journal",
        kwargs={"model": BGPPeerGroup},
    ),
    # Route Policy
    path("route-policy/", RoutePolicyListView.as_view(), name="routepolicy_list"),
    path("route-policy/add/", RoutePolicyEditView.as_view(), name="routepolicy_add"),
    path("route-policy/<int:pk>/", RoutePolicyView.as_view(), name="routepolicy"),
    path(
        "route-policy/<int:pk>/edit/",
        RoutePolicyEditView.as_view(),
        name="routepolicy_edit",
    ),
    path(
        "route-policy/<int:pk>/delete/",
        RoutePolicyDeleteView.as_view(),
        name="routepolicy_delete",
    ),
    path(
        "route-policy/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="routepolicy_changelog",
        kwargs={"model": RoutePolicy},
    ),
    path(
        "route-policy/<int:pk>/journal/",
        ObjectJournalView.as_view(),
        name="routepolicy_journal",
        kwargs={"model": RoutePolicy},
    ),
    # SNMP
    path("snmp/", SNMPListView.as_view(), name="snmp_list"),
    path("snmp/add/", SNMPEditView.as_view(), name="snmp_add"),
    path(
        "snmp/<int:pk>/edit/",
        SNMPEditView.as_view(),
        name="snmp_edit",
    ),
    path(
        "snmp/<int:pk>/delete/",
        SNMPDeleteView.as_view(),
        name="snmp_delete",
    ),
    path(
        "snmp/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="snmp_changelog",
        kwargs={"model": SNMP},
    ),
    # SNMP Community
    path("snmp-community/", SNMPCommunityListView.as_view(), name="snmpcommunity_list"),
    path("snmp-community/add/", SNMPCommunityEditView.as_view(), name="snmpcommunity_add"),
    path(
        "snmp-community/<int:pk>/edit/",
        SNMPCommunityEditView.as_view(),
        name="snmpcommunity_edit",
    ),
    path(
        "snmp-community/<int:pk>/delete/",
        SNMPCommunityDeleteView.as_view(),
        name="snmpcommunity_delete",
    ),
    path(
        "snmp-community/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="snmpcommunity_changelog",
        kwargs={"model": SNMPCommunity},
    ),
    # Device Interface
    path("device-interface/", DeviceInterfaceListView.as_view(), name="deviceinterface_list"),
    path("device-interface/add/", DeviceInterfaceEditView.as_view(), name="deviceinterface_add"),
    path("device-interface/<int:pk>/", DeviceInterfaceView.as_view(), name="deviceinterface"),
    path(
        "device-interface/<int:pk>/edit/",
        DeviceInterfaceEditView.as_view(),
        name="deviceinterface_edit",
    ),
    path(
        "device-interface/<int:pk>/delete/",
        DeviceInterfaceDeleteView.as_view(),
        name="deviceinterface_delete",
    ),
    path(
        "device-interface/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="deviceinterface_changelog",
        kwargs={"model": DeviceInterface},
    ),
    path(
        "device-interface/<int:pk>/journal/",
        ObjectJournalView.as_view(),
        name="deviceinterface_journal",
        kwargs={"model": DeviceInterface},
    ),
    # Logical Interface
    path("logical-interface/", LogicalInterfaceListView.as_view(), name="logicalinterface_list"),
    path("logical-interface/add/", LogicalInterfaceEditView.as_view(), name="logicalinterface_add"),
    path("logical-interface/<int:pk>/", LogicalInterfaceView.as_view(), name="logicalinterface"),
    path(
        "logical-interface/<int:pk>/edit/",
        LogicalInterfaceEditView.as_view(),
        name="logicalinterface_edit",
    ),
    path(
        "logical-interface/<int:pk>/delete/",
        LogicalInterfaceDeleteView.as_view(),
        name="logicalinterface_delete",
    ),
    path(
        "logical-interface/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="logicalinterface_changelog",
        kwargs={"model": LogicalInterface},
    ),
    path(
        "logical-interface/<int:pk>/journal/",
        ObjectJournalView.as_view(),
        name="logicalinterface_journal",
        kwargs={"model": LogicalInterface},
    ),
    # VRF
    path("vrf/", VRFListView.as_view(), name="vrf_list"),
    path("vrf/add/", VRFEditView.as_view(), name="vrf_add"),
    path("vrf/<int:pk>/", VRFView.as_view(), name="vrf"),
    path("vrf/<int:pk>/edit/", VRFEditView.as_view(), name="vrf_edit"),
    path("vrf/<int:pk>/delete/", VRFDeleteView.as_view(), name="vrf_delete"),
    path(
        "vrf/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="vrf_changelog",
        kwargs={"model": VRF},
    ),
    path(
        "vrf/<int:pk>/journal/",
        ObjectJournalView.as_view(),
        name="vrf_journal",
        kwargs={"model": VRF},
    ),
    # VLAN
    path("vlan/", VLANListView.as_view(), name="vlan_list"),
    path("vlan/add/", VLANEditView.as_view(), name="vlan_add"),
    path("vlan/<int:pk>/", VLANView.as_view(), name="vlan"),
    path("vlan/<int:pk>/edit/", VLANEditView.as_view(), name="vlan_edit"),
    path("vlan/<int:pk>/delete/", VLANDeleteView.as_view(), name="vlan_delete"),
    path(
        "vlan/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="vlan_changelog",
        kwargs={"model": VLAN},
    ),
    path(
        "vlan/<int:pk>/journal/",
        ObjectJournalView.as_view(),
        name="vlan_journal",
        kwargs={"model": VLAN},
    ),
    # Link
    path("link/", LinkListView.as_view(), name="link_list"),
    path("link/add/", LinkEditView.as_view(), name="link_add"),
    path("link/<int:pk>/", LinkView.as_view(), name="link"),
    path("link/<int:pk>/edit/", LinkEditView.as_view(), name="link_edit"),
    path("link/<int:pk>/delete/", LinkDeleteView.as_view(), name="link_delete"),
    path(
        "link/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="link_changelog",
        kwargs={"model": Link},
    ),
    path(
        "link/<int:pk>/journal/",
        ObjectJournalView.as_view(),
        name="link_journal",
        kwargs={"model": Link},
    ),
]
