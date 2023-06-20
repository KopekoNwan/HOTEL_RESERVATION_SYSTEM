migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ouc9mg423fntace")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "hrdwr3cj",
    "name": "check_in",
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
    "id": "fwbkqesb",
    "name": "check_out",
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
  collection.schema.removeField("hrdwr3cj")

  // remove
  collection.schema.removeField("fwbkqesb")

  return dao.saveCollection(collection)
})
