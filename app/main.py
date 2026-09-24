from app.graph import graph

def main():
    order = {
        "product": "laptop",
        "quantity": 2,

        ## Values filled by nodes
        "is_valid": False,
        "stock_available": False,
        "status":""
    }

    result = graph.invoke(order)

    print("FINAL STATE")
    print("="*20)
    print(result)

if __name__=="__main__":
    main()