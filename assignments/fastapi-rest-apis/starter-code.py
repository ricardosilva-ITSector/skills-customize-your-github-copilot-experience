from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    completed: bool = False


items: list[Item] = []


@app.get("/items")
def list_items() -> list[Item]:
    return items


@app.post("/items", status_code=201)
def create_item(item: Item) -> Item:
    items.append(item)
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
