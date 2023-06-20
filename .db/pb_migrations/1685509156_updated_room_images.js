migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("obbhx5i2333jgko")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "dcoinjtc",
    "name": "classification",
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
  const collection = dao.findCollectionByNameOrId("obbhx5i2333jgko")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "dcoinjtc",
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
