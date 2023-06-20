migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "ji3a7txy",
    "name": "customer_information",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "v8cua5zxvjxe0mo",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": []
    }
  }))

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "91g9r9td",
    "name": "room",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "v8cua5zxvjxe0mo",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": []
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "ji3a7txy",
    "name": "customer_information",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "v8cua5zxvjxe0mo",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "customer_name",
        "customer_id"
      ]
    }
  }))

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "91g9r9td",
    "name": "room",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "v8cua5zxvjxe0mo",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "room_number"
      ]
    }
  }))

  return dao.saveCollection(collection)
})
