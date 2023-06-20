migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ouc9mg423fntace")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "5ex0baxd",
    "name": "room",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "x0hmwdlv02zwb5y",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": []
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("ouc9mg423fntace")

  // remove
  collection.schema.removeField("5ex0baxd")

  return dao.saveCollection(collection)
})
