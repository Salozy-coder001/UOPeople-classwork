# Dictionary containing shipment IDs and statuses
shipments = {
    "SHP101": "Delivered",
    "SHP102": "In Transit",
    "SHP103": "Pending",
    "SHP104": "Delivered"
}

print(shipments)

# Retrieve the status of shipment SHP103
status = shipments["SHP103"]

print(f"Shipment SHP103 status: {status}")