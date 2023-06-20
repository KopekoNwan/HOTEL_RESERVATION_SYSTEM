migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1rm9eqlfw2z6co2")

  // remove
  collection.schema.removeField("csz0bbt0")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1rm9eqlfw2z6co2")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "csz0bbt0",
    "name": "zip_code",
    "type": "number",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null
    }
  }))

  return dao.saveCollection(collection)
})
