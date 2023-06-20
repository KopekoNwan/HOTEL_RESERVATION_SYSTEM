migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ouc9mg423fntace")

  // remove
  collection.schema.removeField("xwxlnwt5")

  // remove
  collection.schema.removeField("nhwbvchr")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ouc9mg423fntace")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "xwxlnwt5",
    "name": "room_number",
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
    "id": "nhwbvchr",
    "name": "room_type",
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
