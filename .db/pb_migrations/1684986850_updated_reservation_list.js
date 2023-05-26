migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "4ol4f7hf",
    "name": "room_type",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "kigjd431nqoyf61",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "type",
        "price"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "4ol4f7hf",
    "name": "room_type",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "kigjd431nqoyf61",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": []
    }
  }))

  return dao.saveCollection(collection)
})
