def validation_order(state):
    print("Validate order")
    product = state["product"]
    quantity = state["quantity"]

    if product and quantity > 0:
        is_valid = True
    else:
        is_valid = False
    
    print("Product: ", product)
    print("Quantity: ", quantity)
    print("Validation o/p: ", is_valid)

    return{
        **state, "is_valid": is_valid
    }

def check_stock(state):
    print("Checking stock")
    product = state["product"]
    quantity = state["quantity"]

    ## Fake inventory
    inventory = {
        "laptop": 5,
        "keyboard": 10,
        "wires": 20,
    } 

    ## Get available stock
    available_stock = inventory.get(product.lower(),0)

    ## check whether requested quantity is available in inventory
    stock_available = available_stock >= quantity

    print("-"*20)
    print("Product: ", product)
    print("Requested: ", quantity)
    print("Available: ", available_stock)
    print("Stock available: ", stock_available)

    return{
        **state, 
        "stock_available" : stock_available,
    }

## Node 3: confirm order

def confirm_order(state):
    print("Confirm order")
    print(
        f"Order confirmed for"
        f"{state["quantity"]} {state['product']}(s)"
    )
    return {
        **state,
        "status": "CONFIRMED"
    }

## Node 4: Reject order
def reject_order(state):
    print("Reject order")
    print(
        "Order cannot be fulfiled"
    )
    return {
        **state,
        "status": "REJECTED"
    }