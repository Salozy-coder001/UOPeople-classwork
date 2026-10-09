# Retrieve the status of shipment SHP103

shipments = {"SHP103": "In transit"}
status = shipments["SHP103"]
print(f"Shipment SHP103 status: {status}")

#adding a new shipment
shipments["SHP105"] = "Pending"

print(shipments)

#removing a completed shipment

del shipments["SHP101"]
print(shipments)

#list all shipment ids
print("Shipment IDs:")
print(shipments.keys())

#list all shipment statuses
print("Shipment Statuses:")
print("Statuses:")
print(shipments.values())

#list all shipment records
print("Shipment Details:")
print(shipments.items())

