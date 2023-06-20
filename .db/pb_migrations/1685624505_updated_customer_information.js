migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1rm9eqlfw2z6co2")

  // remove
  collection.schema.removeField("enzo8257")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1rm9eqlfw2z6co2")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "enzo8257",
    "name": "address",
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
