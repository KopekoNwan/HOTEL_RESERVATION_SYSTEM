migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ouc9mg423fntace")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "xri9hzu4",
    "name": "reservation_id",
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
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ouc9mg423fntace")

  // remove
  collection.schema.removeField("xri9hzu4")

  return dao.saveCollection(collection)
})
