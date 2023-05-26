migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("x0hmwdlv02zwb5y")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "puqfzip3",
    "name": "room",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "kigjd431nqoyf61",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "type",
        "price"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("x0hmwdlv02zwb5y")

  // remove
  collection.schema.removeField("puqfzip3")

  return dao.saveCollection(collection)
})
