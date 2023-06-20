migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "xyrkc852",
    "name": "email",
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
    "id": "pz3x7foh",
    "name": "contact",
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
  const collection = dao.findCollectionByNameOrId("oeyxxgviihyuhu4")

  // remove
  collection.schema.removeField("xyrkc852")

  // remove
  collection.schema.removeField("pz3x7foh")

  return dao.saveCollection(collection)
})
