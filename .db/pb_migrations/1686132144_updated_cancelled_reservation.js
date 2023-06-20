migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // remove
  collection.schema.removeField("gcwzqj2v")

  // remove
  collection.schema.removeField("yaikzyni")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "gcwzqj2v",
    "name": "room",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "yaikzyni",
    "name": "checkIn_checkOut",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
})
