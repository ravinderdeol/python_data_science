order_9423517 = {
    "OrderNo": 9423517,
    "Date": "2022-02-04",
    "EmpNo": 9001
}

extra_fields_9423517 = {
    "ShippingInstructions": {
        "name": "John Silver",
        "phone": [
            {
                "type": "Office", "number": "809-123-9309",
                "type": "Mobile", "number": "417-123-4567"
            }
        ]
    }
}

# combine two dictionaries by unpacking them then store the results in a new dictionary
order_9423517 = {**order_9423517, **extra_fields_9423517}

print(order_9423517)

# notes
    # '**' unpacks a dictionary into its individual key value pairs
    # combine two dictionaries by unpacking them then store the results in a new dictionary
    # accessing data by keys rather than positions makes dictionaries preferable for hierarchical data
