from flask import Blueprint
from models import Zone

zone_bp = Blueprint(
    "zones",
    __name__,
    url_prefix="/api"
)

@zone_bp.route("/zones")
def zones():

    zones = Zone.query.all()

    result = []

    for zone in zones:

        result.append({
            "id": zone.location_id,
            "borough": zone.borough,
            "zone": zone.zone_name,
            "service_zone": zone.service_zone
        })

    return result