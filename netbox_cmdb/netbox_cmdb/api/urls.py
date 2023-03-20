from django.urls import path
from netbox.api.routers import NetBoxRouter

from netbox_cmdb.api.bgp.views import (
    ASNViewSet,
    AvailableASNsView,
    BGPGlobalViewSet,
    BGPPeerGroupViewSet,
    BGPSessionsViewSet,
)
from netbox_cmdb.api.bgp_community_list.views import BGPCommunityListViewSet
from netbox_cmdb.api.prefix_list.views import PrefixListViewSet
from netbox_cmdb.api.route_policy.views import RoutePolicyViewSet

router = NetBoxRouter()

router.register("asns", ASNViewSet)
router.register("bgp-global", BGPGlobalViewSet)
router.register("bgp-sessions", BGPSessionsViewSet)
router.register("bgp-community-lists", BGPCommunityListViewSet)
router.register("peer-groups", BGPPeerGroupViewSet)
router.register("prefix-lists", PrefixListViewSet)
router.register("route-policies", RoutePolicyViewSet)

urlpatterns = [
    path(
        "asns/available-asn/",
        AvailableASNsView.as_view(),
        name="asns-available-asn",
    ),
]
urlpatterns += router.urls