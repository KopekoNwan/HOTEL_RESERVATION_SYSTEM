migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("x0hmwdlv02zwb5y")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "kbx3dd4k",
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

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "f1zhs8eh",
    "name": "price",
    "type": "number",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("x0hmwdlv02zwb5y")

  // remove
  collection.schema.removeField("kbx3dd4k")

  // remove
  collection.schema.removeField("f1zhs8eh")

  return dao.saveCollection(collection)
})
