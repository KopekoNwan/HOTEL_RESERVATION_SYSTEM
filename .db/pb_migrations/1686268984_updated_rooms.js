migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("x0hmwdlv02zwb5y")

  // remove
  collection.schema.removeField("kbx3dd4k")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "jv9qapf6",
    "name": "room_type",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "kigjd431nqoyf61",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": [
        "type"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
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

  // remove
  collection.schema.removeField("jv9qapf6")

  return dao.saveCollection(collection)
})
