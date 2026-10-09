shipments = {
    "SHP001": {
        "destination": "Lagos",
        "status": "In Transit",
        "delivery_date": "2026-10-15"
    },
    "SHP002": {
        "destination": "Abuja",
        "status": "Delivered",
        "delivery_date": "2026-10-10"
    },
    "SHP003": {
        "destination": "Port Harcourt",
        "status": "Pending",
        "delivery_date": "2026-10-18"
    }
}

#This structure allows quick access to shipment information using the shipment ID as the key
print(shipments["SHP001"]["status"])

#Updating information is also straightforward:
shipments["SHP001"]["status"] = "Delivered"
print(shipments["SHP001"]["status"])

#Searching for shipments going to a particular city can be done by iterating through the dictionary:
for shipment_id, details in shipments.items():
    if details["destination"] == "Abuja":
        print(shipment_id)