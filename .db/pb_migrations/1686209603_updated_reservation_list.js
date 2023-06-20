migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "oymko3so",
    "name": "state",
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
  const collection = dao.findCollectionByNameOrId("v8cua5zxvjxe0mo")

  // remove
  collection.schema.removeField("oymko3so")

  return dao.saveCollection(collection)
})
