migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ouc9mg423fntace")

  // remove
  collection.schema.removeField("hrdwr3cj")

  // remove
  collection.schema.removeField("fwbkqesb")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "nnva3ai3",
    "name": "check_in",
    "type": "date",
    "required": false,
    "unique": false,
    "options": {
      "min": "",
      "max": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "evgs6s9a",
    "name": "check_out",
    "type": "date",
    "required": false,
    "unique": false,
    "options": {
      "min": "",
      "max": ""
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
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

  // remove
  collection.schema.removeField("nnva3ai3")

  // remove
  collection.schema.removeField("evgs6s9a")

  return dao.saveCollection(collection)
})
