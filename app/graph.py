from langgraph.graph import StateGraph, END
from app.state import OrderState

from app.nodes import (validation_order,check_stock, confirm_order, reject_order)
from app.edges import stock_router

## Step 1: Create the graph- telling the LangGraph about what shared state looks like
workflow = StateGraph(OrderState)

## Step 2: Add nodes to the workflow
workflow.add_node("validate", validation_order)

workflow.add_node("check_stock", check_stock)

workflow.add_node("confirm", confirm_order)

workflow.add_node("reject", reject_order)

## Step 3: Define starting point
workflow.set_entry_point("validate")

## Step 4: Define edges
workflow.add_edge("validate", "check_stock")

workflow.add_conditional_edges("check_stock",stock_router)

## Step 5: Define ending nodes
workflow.add_edge("confirm", END)

workflow.add_edge("reject",END)

## Step 6: Compile Graph
graph = workflow.compile()