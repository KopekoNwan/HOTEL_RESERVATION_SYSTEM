migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "ui2moic5",
    "name": "room_number",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "x0hmwdlv02zwb5y",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "room_number"
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
    "id": "ui2moic5",
    "name": "room_number",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "x0hmwdlv02zwb5y",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "room_number",
        "room_type"
      ]
    }
  }))

  return dao.saveCollection(collection)
})
